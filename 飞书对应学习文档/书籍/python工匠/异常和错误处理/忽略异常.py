#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/24


class ignore_closed:
    """忽略已经关闭的连接"""
    def __enter__(self):
        pass
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type == AlreadyClosedError:
            return True
        return False