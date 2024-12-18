#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/11/30
# 文件名称   ：delayedStart.PY
from functools import update_wrapper
import time

class DelayedStart:
    """在执行被装饰函数前，等待 1 秒钟"""
    def __init__(self, func):
        update_wrapper(self, func)
        self.func = func
    def __call__(self, *args, **kwargs):
        print(f'Wait for 1 second before starting...')
        time.sleep(1)
        return self.func(*args, **kwargs)
    def eager_call(self, *args, **kwargs):
        """跳过等待，立刻执行被装饰函数"""
        print('Call without delay')
        return self.func(*args, **kwargs)

@DelayedStart
def hello():
    print('hello world!')

print(hello) #<__main__.DelayedStart object at 0x0000018BBA84DF70>  代表hello函数变成了装饰类DeLayedStart的实例

print(type(hello)) #<class '__main__.DelayedStart'>
print(hello.__name__) #hello

#Wait for 1 second before starting...
# hello world!
hello()  #会触发装饰类DelayedStart的__call__方法


#Call without delay
# hello world!
hello.eager_call()  #会使用额外的eager_call方法
