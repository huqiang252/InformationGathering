#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/19

from sqlalchemy import create_engine, select, Table, MetaData

def fetch_users_v2(
    conn,
    min_level=None,
    gender=None,
    has_membership=False,
    sort_field="created",
):
    """获取用户列表"""
    query = select([users.c.id, users.c.name])
    if min_level is not None:
        query = query.where(users.c.level >= min_level)
    if gender is not None:
        query = query.where(users.c.gender == gender)
    query = query.where(users.c.has_membership == has_membership).order_by(
        users.c[sort_field]
    )
    return list(conn.execute(query))

# 创建数据库引擎
engine = create_engine('sqlite:///example.db')

# 创建元数据对象
metadata = MetaData()

# 加载表定义
users = Table('users', metadata, autoload_with=engine)

# 创建数据库连接
conn = engine.connect()

# 示例参数
min_level = 5
gender = 'male'
has_membership = True
sort_field = 'name'

# 调用函数
users_list = fetch_users_v2(conn, min_level=min_level, gender=gender, has_membership=has_membership, sort_field=sort_field)

# 打印结果
for user in users_list:
    print(user)

# 关闭连接
conn.close()
