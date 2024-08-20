#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-07-27
import time

def count_time(func):
    def inner():
        start_time = time.time()
        func()
        stop_time = time.time()
        print(f'函数执行的时间为：{stop_time-start_time}秒')
    return inner


@count_time
def show():
    for i in range(3):
        print(f'第{i+1}次输出')
        time.sleep(1)


if __name__ == '__main__':
    show()