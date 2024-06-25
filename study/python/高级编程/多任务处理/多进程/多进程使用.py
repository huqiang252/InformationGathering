#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-06-24
import multiprocessing
import time,os


# 跳舞任务
def task1():
    # print(multiprocessing.current_process()) #当前进程
    print(multiprocessing.current_process().name) #获取进程名称
    print(f"{multiprocessing.current_process().name}_ID", os.getpid())
    print(f"{multiprocessing.current_process().name}_Parent_ID", os.getppid())
    for i in range(5):
        print("跳舞中...")
        time.sleep(0.2)


# 唱歌任务
def task2():
    # print(multiprocessing.current_process()) #当前进程
    print(multiprocessing.current_process().name)
    print(f"{multiprocessing.current_process().name}_ID", os.getpid())
    print(f"{multiprocessing.current_process().name}_Parent_ID", os.getppid())

    for i in range(5):
        print("唱歌中...")
        time.sleep(0.2)




if __name__ == '__main__':
    print(f"{multiprocessing.current_process().name}_ID", os.getpid())  #主进程  --当前进程ID
    print(f"{multiprocessing.current_process().name}_Parent_ID", os.getppid()) # ---当前父进程ID
    p1 = multiprocessing.Process(target=task1, name="myprocess1")
    p2 = multiprocessing.Process(target=task2)
    p1.start()
    p2.start()
