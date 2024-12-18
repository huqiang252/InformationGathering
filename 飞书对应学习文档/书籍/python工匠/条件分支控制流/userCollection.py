#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/24


class UserCollection:
    """用于保存多个用户的集合工具类"""

    def __init__(self, users):
        self.items = users

    def __len__(self):
        return len(self.items)

users = UserCollection(['piglei', 'raymond'])

# 不需要手动判断内部items的长度
if users :
    print("There's some users in collection!")

if __name__ == '__main__':
    users2= UserCollection([])
    print(len(users2)) #0

    users3 = UserCollection(['piglei','xipl','sljf'])
    print(len(users3)) #3