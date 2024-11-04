#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/29


class TestResource:
    def __init__(self):
        self._user_service = None
        self._app_ui = None
        self._accounts = None
        self._db_mysql = None

        self._active_components = []

    def __del__(self):
        self.cleanup()

    def cleanup(self):
        for resource_item in self._active_components:
            resource_item.cleanup()

    @property
    def user_service(self):
        if not self._user_service:
            self._user_service = UserService()
            self._active_components.append(self._user_service)
        return self._user_service