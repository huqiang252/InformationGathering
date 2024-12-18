#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/24


from contextlib import contextmanager
@contextmanager
def create_conn_obj(host, port, timeout=None):
    """创建连接对象，并在退出上下文时自动关闭"""
    conn = create_conn(host, port, timeout=timeout)
    try:
        yield conn
    finally:
        conn.close()