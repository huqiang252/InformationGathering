#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2025/1/12
# 文件名称   ：contextmanager模拟上下文.py


import contextlib

from 飞书对应学习文档.编写整洁的python代码.python惯用法.上下文管理器 import stop_database, start_database,db_backup


@contextlib.contextmanager
def db_handler():
    try:
        stop_database()
        yield
    finally:
        start_database()


with db_handler:
    db_backup()




