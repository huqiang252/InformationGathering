#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/2
# 文件名称   ：user.py
from collections.abc import Iterable

class DeactivationNotSupported(Exception):
    """当用户不支持停用时抛出"""

class User():
    """用户类，包含普通用户的相关操作"""
    ...
    def __init__(self,username):
        self.username = username
        self.is_active = True
    def save(self):
        """保存用户信息"""
        ...

    def deactivate(self):
        """停用当前用户"""
        print(f'{self.username} is deactivate')
        self.is_active = False
        self.save()


class Admin(User):
    """管理员用户类"""


    def deactivate(self):
        # 管理员用户不允许被停用
        raise DeactivationNotSupported('admin can not be deactivated!')


def deactivate_users(users:Iterable[User]):
    """批量停用用户
    :param users:可迭代的用户对象 User
    """
    for user in users:
        try:
            user.deactivate()
        except DeactivationNotSupported:
            print(f'{user.username} does not alllow deactivating,skip')



if __name__ == '__main__':
    deactivate_users([User(username='user1'),Admin(username='admin'),User(username='user2')])
