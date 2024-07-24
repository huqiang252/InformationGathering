import mysql.connector
import cx_Oracle
import decimal
import datetime

class DatabaseClient2:
    def __init__(self, database_type, dsn=None):
        self.database_type = database_type
        self.dsn = dsn
        self.connection = None
        self.cursor = None

    def connect(self, host=None, port=None, username=None, password=None, database=None):
        # Connection setup based on database type
        pass

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
        if query_data is None:
            return None

        columns = [col[0] for col in self.cursor.description]
        return {col: self.convert_value(val) for col, val in zip(columns, query_data)}

    def convert_value(self, val):
        if isinstance(val, decimal.Decimal):
            return float(val)
        elif isinstance(val, (datetime.datetime, datetime.date)):
            return val.isoformat()
        elif isinstance(val, bytes):
            return val.decode('utf-8', errors='ignore')
        else:
            return val

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
    with DatabaseClient2('MySQL') as db:
        db.connect(host='mysql-hs-hq-daily.hszq8.com', port=3306, username='hq_basedata', password='hq_basedata', database='hq_basedata')

        # db.execute(
        #     f"select split_date,split_factor from quote_basic_split where security_code = '{security_code}' and split_date>='{start_split_date}' order by split_date desc")

        db.execute(
            f"select * from quote_basic_split where security_code = '{security_code}' and split_date>='{start_split_date}' order by split_date desc")

        rows = db.fetchall()

        # print(rows)
        for row in rows:
            print(row)