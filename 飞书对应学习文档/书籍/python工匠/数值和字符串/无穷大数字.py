#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/19



def sort_users_inf(users):
    # 定义一个键函数，用于排序
    key_func = lambda username: users[username] if users[username] is not None else float('inf')

    # 使用 sorted 函数进行排序
    return sorted(users.keys(), key=key_func)

users = {"tom": 19, "jenny": 13, "jack": None, "andrew": 43}
print(sort_users_inf(users))
# 输出：
# ['jenny', 'tom', 'andrew', 'jack']
