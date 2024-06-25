#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-06-24
import threading
import time

# 创建互斥锁
lock = threading.Lock()

numbers = [3, 6, 8, 1, 9]

# 根据下标去取值， 保证同一时刻只能有一个线程去取值
def get_value(index):
    # 上锁
    lock.acquire()
    # 判断下标释放越界
    if index >= len(numbers):
        print(threading.current_thread().name, f"下标 {index} 越界")
        lock.release()
        return
    value = numbers[index]
    print(threading.current_thread().name, "取值为： ", value)

    time.sleep(0.2)
    # 释放锁
    lock.release()


if __name__ == '__main__':
    # 模拟大量线程去执行取值操作
    for i in range(10):
        sub_thread = threading.Thread(target=get_value, args=(i,))
        sub_thread.start()
