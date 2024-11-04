#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/28


# test resource:
class TestResource:
    def __init__(self):
        self._db_mysql = None
        ...

    @property
    def database(self):
        if not self._db_mysql:
            self._db_mysql = QaMySql()
            self._db_mysql.connect()
        return self._db_mysql

    @property
    def user_service(self):
        if not self._user_service:
            self._user_service = QaUserService()
        return self._user_service

# test case:
def test_case_1(resources):
    ...
    resources.user_service.create_new_user(user_data)
    ...