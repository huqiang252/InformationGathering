import datetime
import decimal

import mysql.connector
import cx_Oracle



class Database:
    '''
    需要安装库
    pip install mysql-connector-python
    pip install cx_Oracle
    '''
    def __init__(self, database_type):
        self.database_type = database_type
        self.host = None
        self.port = None
        self.username = None
        self.password = None
        self.database = None
        self.connection = None
        self.cursor = None

    def connect(self, host, port, username, password, database):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database

        if self.database_type == 'MySQL':
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.username,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()

        elif self.database_type == 'Oracle':
            dsn = cx_Oracle.makedsn(self.host, self.port, self.database)
            self.connection = cx_Oracle.connect(
                user=self.username,
                password=self.password,
                dsn=dsn
            )
            self.cursor = self.connection.cursor()

        return self

    def execute(self, query):
        self.cursor.execute(query)
        return self

    def fetchall(self):
        # return self.cursor.fetchall()
        query_datas = self.cursor.fetchall()
        result=[]
        for query_data in query_datas:
            result.append(self.sql_data_handler(query_data))
        return result  #返回格式化后的列表数据

    def fetchone(self):
        # return self.cursor.fetchone()
        query_data = self.cursor.fetchone()
        return self.sql_data_handler(query_data)  #返回格式化后的列表数据

    def commit(self):
        self.connection.commit()
        return self

    def rollback(self):
        self.connection.rollback()
        return self

    def disconnect(self):
        self.cursor.close()
        self.connection.close()
        return self

    def sql_data_handler(self, query_data):
        """
        处理部分类型sql查询出来的数据格式
        @param query_data: 查询出来的sql数据
        @return:列表数据
        """
        # 将sql 返回的所有内容全部放入对象中
        query_data_list=[]

        for index in range(len(query_data)):
            if isinstance(query_data[index], decimal.Decimal):
                value = float(query_data[index])
            elif isinstance(query_data[index], datetime.datetime):
                value = str(query_data[index])
            elif isinstance(query_data[index], datetime.date):
                value = str(query_data[index])
            else:
                value=query_data[index]
            query_data_list.append(value)
        return query_data_list

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

if __name__ == '__main__':
    db = Database('MySQL').connect('mysql-hs-hq-daily.hszq8.com', 3306, 'hq_basedata', 'hq_basedata',
                                   'hq_basedata')

    security_code = "03187.HK"
    start_split_date="2023-02-28"
    result = db.execute(
        f"select split_date,split_factor from quote_basic_split where security_code = '{security_code}' and split_date>='{start_split_date}' order by split_date desc").fetchall()

    print(result)