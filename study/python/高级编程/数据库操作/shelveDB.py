#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : tony
import shelve


class ShelveDB:
    def __init__(self, db_file):
        self.db_file=db_file
        print(f'打开自带数据库目录：{db_file}')
        self.db = shelve.open(db_file)


    def get(self, key):
        print(f'成功获取数据库：{self.db_file}的{key}的值为{self.db[key]}')
        return self.db[key]

    def set(self, key, value):
        self.db[key] = value
        print(f'成功设置数据库：{self.db_file}的{key}的值为{value}')

    def delete(self, key):
        del self.db[key]
        print(f'成功删除数据库：{self.db_file}的{key}')

    def close(self):
        self.db.close()
        print(f'自带数据库{self.db_file}已关闭')




if __name__ == '__main__':

     # 创建一个数据库对象
    db = ShelveDB('mydb.db')
     # 向数据库中添加一条记录
    db.set('name', 'John Doe')
     # 从数据库中读取一条记录
    name = db.get('name')
     # 删除一条记录
    db.delete('name')
     # 关闭数据库
    db.close()


