import datetime
import decimal

import mysql.connector
import cx_Oracle


class DatabaseClient:
    '''
    需要安装库
    pip install mysql-connector-python
    pip install cx_Oracle
    '''
    def __init__(self, database_type, dsn=None):
        self.database_type = database_type
        self.dsn = dsn
        self.connection = None
        self.cursor = None

    def connect(self, host=None, port=None, username=None, password=None, database=None):
        if self.database_type == 'MySQL':
            self.connection = mysql.connector.connect(
                host=host,
                port=port,
                user=username,
                password=password,
                database=database
            )
        elif self.database_type == 'Oracle':
            if not self.dsn:
                self.dsn = cx_Oracle.makedsn(host, port, database)
            self.connection = cx_Oracle.connect(
                user=username,
                password=password,
                dsn=self.dsn
            )
        self.cursor = self.connection.cursor()
        return self

    def execute(self, query):
        self.cursor.execute(query)
        return self

    def fetchall(self):
        query_datas = self.cursor.fetchall()
        return [self.sql_data_handler(query_data) for query_data in query_datas]

    def fetchone(self):
        query_data = self.cursor.fetchone()
        return self.sql_data_handler(query_data)

    def commit(self):
        self.connection.commit()
        return self

    def rollback(self):
        self.connection.rollback()
        return self

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        return self

    def sql_data_handler(self, query_data):
        if isinstance(query_data, (list, tuple)):
            return [self.sql_data_handler(item) for item in query_data]
        elif isinstance(query_data, decimal.Decimal):
            return float(query_data)
        elif isinstance(query_data, (datetime.datetime, datetime.date)):
            return query_data.isoformat()
        elif isinstance(query_data, bytes):
            return query_data.decode('utf-8', errors='ignore')
        else:
            return query_data

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()
        if exc_type:
            print(f"An error occurred: {exc_type}, {exc_val}, {exc_tb}")


if __name__ == '__main__':


    # MySQL 连接示例
    security_code = "03187.HK"
    start_split_date = "2023-02-28"
    with DatabaseClient('MySQL') as db:
        db.connect(host='mysql-hs-hq-daily.hszq8.com', port=3306, username='hq_basedata', password='hq_basedata', database='hq_basedata')

        # db.execute(
        #     f"select split_date,split_factor from quote_basic_split where security_code = '{security_code}' and split_date>='{start_split_date}' order by split_date desc")

        db.execute(
            f"select * from quote_basic_split where security_code = '{security_code}' and split_date>='{start_split_date}' order by split_date desc")

        rows = db.fetchall()

        # print(rows)
        for row in rows:
            print(row)

    # Oracle 连接示例
    # with Database('Oracle', dsn='host:port/service_name') as db:
    #     db.connect(username='user', password='pass')
    #     db.execute("SELECT * FROM mytable")
    #     rows = db.fetchall()
    #     for row in rows:
    #         print(row)