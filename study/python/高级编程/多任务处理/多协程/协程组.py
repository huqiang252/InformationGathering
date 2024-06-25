#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-06-24
import gevent

def task():
    for i in range(1,3):
        print(gevent.getcurrent())
        print(i)
        gevent.sleep(0.001) #模拟耗时

# 使用列表推导式，生成一个有5个协程对象的列表
gs = [gevent.spawn(task) for i in range(5)]
gevent.joinall(gs)
