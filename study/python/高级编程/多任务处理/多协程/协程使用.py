#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-06-24
import gevent

def task():
    for i in range(1,3):
        print(gevent.getcurrent(), i) #协程对象
        print(i)

g1 = gevent.spawn(task)
g2 = gevent.spawn(task)
g3 = gevent.spawn(task)


g1.join()
g2.join()
g3.join()
print("main")