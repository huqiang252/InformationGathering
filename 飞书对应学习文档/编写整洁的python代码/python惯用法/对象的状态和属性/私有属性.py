#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2025/1/12
# 文件名称   ：私有属性.py

class Connector:
    def __init__(self, source):
        self.source = source
        self._timeout=60

if __name__ == '__main__':
    conn = Connector('postgresql://localhost')
    print(conn.source)
    print(conn._timeout)
    print(conn.__dict__) #{'source': 'postgresql://localhost', '_timeout': 60}