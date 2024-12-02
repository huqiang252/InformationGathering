#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/2
# 文件名称   ：user.py


class User(Model):
    """用户类，包含普通用户的相关操作"""

    ...

    def deactivate(self):
        """停用当前用户"""
        self.is_active = False
        self.save()


class Admin(User):
    """管理员用户类"""
    ...
    def deactivate(self):
        # 管理员用户不允许被停用
        raise RuntimeError('admin can not be deactivated!')

from collections import Iterable
def deactivate_users(users:Iterable[User]):
    """批量停用用户
    :param users:可迭代的用户对象 User
    """
    for user in users:
        user.deactivate()