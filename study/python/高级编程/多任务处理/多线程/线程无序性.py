#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-06-24


import threading
import time
def task():
    time.sleep(1)
    print("当前线程:", threading.current_thread().name)

if __name__ == '__main__':

   for _ in range(5):
       t = threading.Thread(target=task)
       t.start()
