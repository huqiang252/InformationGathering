#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-06-24
import gevent  #pip install gevent

def task(n, msg):
    for i in range(1,n+1):
        print(gevent.getcurrent(), f"第 {i} 次输出 {msg}")
        gevent.sleep(0.001)

g1 = gevent.spawn(task,5, "Python")
g2 = gevent.spawn(task, msg="Hogwarts", n=5)
g1.join()
g2.join()
