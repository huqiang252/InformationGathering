#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/28


# TestResource.py
class TestResource:

    def __init__(self):
        self._order_service = None
        self._db_mysql = None
        # ...
        self.initialize()

    def __del__(self):
        self.cleanup()

    def initialize(self):
        ...

    def cleanup(self):
        ...

    @property
    def user_service(self):
        if not self._user_service:
            self._user_service = UserService()
        return self._user_service

    @property
    def order_service(self):
        if not self._order_service:
            self._order_service = OrderService()
        return self._order_service

    @property
    def database(self):
        if not self._db_mysql:
            self._db_mysql = QaMysql()
            self._db_mysql.connect()

        return self._db_mysql