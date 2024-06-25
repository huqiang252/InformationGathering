#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-06-24
import time
import threading

# 定义全局变量
sum = 0

lock = threading.Lock()

# 方式一
def add_one():
    global sum
    lock.acquire()
    for i in range(1000000):
        sum += 1
    lock.release()
    print(threading.current_thread().name , " : ", sum)

# 方式二
# def add_one():
#     global sum
#     for i in range(1000000):
#         lock.acquire()
#         sum += 1
#         lock.release()
#     print(threading.current_thread().name , " : ", sum)


if __name__ == '__main__':
    # 创建两个线程
    t1 = threading.Thread(target=add_one)
    t2 = threading.Thread(target=add_one)
    t3 = threading.Thread(target=add_one)

    # 启动线程
    t1.start()
    t2.start()
    t3.start()
    time.sleep(3)
    print(threading.current_thread().name , " : ", sum)
