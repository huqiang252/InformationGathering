#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-06-24
import threading
import time
def task(n, msg):
    for i in range(n):
        print(threading.current_thread().name, f"打印第 {i+1} 次 {msg}")
        time.sleep(0.2)

if __name__ == '__main__':

    t1 = threading.Thread(target=task, args=(10, "Python"),daemon=True)
    t2 = threading.Thread(target=task, kwargs={"n": 10, "msg": "Hogwarts"})
    t2.daemon = True
    t1.start()
    t2.start()
    time.sleep(1)
    print("main")
