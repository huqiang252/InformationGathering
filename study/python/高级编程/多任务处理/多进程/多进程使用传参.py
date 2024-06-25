#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-06-24
import multiprocessing
import time
def task(n, msg):
    for i in range(n):
        print(multiprocessing.current_process().name, f"打印第 {i+1} 次 {msg}")
        time.sleep(0.2)

if __name__ == '__main__':
    # 使用可变位置参数传参
    p1 = multiprocessing.Process(target=task, args=(10, "Python"))
    # 使用可变关键字参数传参
    p2 = multiprocessing.Process(target=task, kwargs={"n": 10, "msg": "Hogwarts"})
    p1.start()
    p2.start()
