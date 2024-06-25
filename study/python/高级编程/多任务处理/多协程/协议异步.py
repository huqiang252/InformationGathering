#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-06-24


from gevent import monkey
monkey.patch_all()
import gevent
import random


'''
在 Python3.10 版本中，Gevent 的 monkey patch 功能在某些情况下可能无效。
这是因为在 Python3.10 中引入了 asyncio 的新的事件循环机制，与 Gevent 的事件循环有所不同，导致 monkey patch 在有些情况下失效。
Gevent 官方还没有正式发布兼容 Python3.10 版本的版本，因此在 Python3.10 中使用 monkey.patch_all() 方法可能无法正常实现非阻塞的协程 I/O。
为了解决这个问题，你可以考虑使用 Python3.10 引入的 asyncio 模块来进行异步编程。
asyncio 提供了原生的协程和事件循环，可以实现高效的异步操作
'''

def task(n, msg):
    for i in range(1,n+1):
        print(gevent.getcurrent(), f"第 {i} 次输出 {msg}")
        gevent.sleep(random.random())


g1 = gevent.spawn(task,5, "Python")
g2 = gevent.spawn(task, msg="Hogwarts", n=5)
g3 = gevent.spawn(task, n=5, msg="Hello")
gevent.joinall((g1,g2,g3))
