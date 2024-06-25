#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-06-24
import threading
import time

# 定义全局变量
g_list = list()


# 添加数据的任务
def add_data():
    for i in range(5):
        g_list.append(i)
        print("add:", i)
        time.sleep(0.2)

    print("add_data:", g_list)


def read_data():
    print("read_data", g_list)


if __name__ == '__main__':
    add_data_Thread = threading.Thread(target=add_data)
    read_data_Thread = threading.Thread(target=read_data)

    add_data_Thread.start()
    add_data_Thread.join()
    read_data_Thread.start()

    print("main:", g_list)
