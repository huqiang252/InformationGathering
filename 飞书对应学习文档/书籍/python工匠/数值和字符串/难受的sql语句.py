#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/18


def fetch_users(
    conn,
    min_level=None,
    gender=None,
    has_membership=False,
    sort_field="created",
):
    """获取用户列表

    :param min_level: 要求的最低用户级别，默认为所有级别
    :type min_level: int, optional
    :param gender: 筛选用户性别，默认为所有性别
    :type gender: int, optional
    :param has_membership: 筛选会员或非会员用户，默认为 False，代表非会员
    :type has_membership: bool, optional
    :param sort_field: 排序字段，默认为 "created"，代表按用户创建日期排序
    :type sort_field: str, optional
    :return: 一个包含用户信息的列表：[(User ID, User Name), ...]
    """
    # 一种古老的SQL 拼接技巧，使用“WHERE 1=1”来简化字符串拼接操作
    statement = "SELECT id, name FROM users WHERE 1=1"
    params = []
    if min_level is not None:
        statement += " AND level >= ?"
        params.append(min_level)
    if gender is not None:
        statement += " AND gender >= ?"
        params.append(gender)
    if has_membership:
        statement += " AND has_membership = true"
    else:
        statement += " AND has_membership = false"

    statement += " ORDER BY ?"
    params.append(sort_field)
    # 将查询参数 params 作为位置参数传递，避免 SQL 注入问题
    return list(conn.execute(statement, params))