#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-06-24



import threading
import time


# 跳舞任务
def task1():
    print(threading.current_thread().name)
    for i in range(5):
        print("跳舞中...")
        time.sleep(0.2)


# 唱歌任务
def task2():
    print(threading.current_thread().name)
    for i in range(5):
        print("唱歌中...")
        time.sleep(0.2)

if __name__ == '__main__':
    print(threading.current_thread().name)
    t1 = threading.Thread(target=task1, name="mythread-1")
    t2 = threading.Thread(target=task2)
    t1.start()
    t2.start()