#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/11/30
# 文件名称   ：delayedStarthasPramas.PY
import functools
import time
from functools import update_wrapper

class DelayedStart:
    """在执行被装饰函数前，等待一段时间
    :param func: 被装饰的函数
    :param duration: 需要等待的秒数
    """
    def __init__(self, func, *, duration=1):
        update_wrapper(self, func)
        self.func = func
        self.duration = duration
    def __call__(self, *args, **kwargs):
        print(f'Wait for {self.duration} second before starting...')
        time.sleep(self.duration)
        return self.func(*args, **kwargs)
    def eager_call(self, *args, **kwargs):
        """跳过等待，立刻执行被装饰函数"""
        print('Call without delay')
        return self.func(*args, **kwargs)
def delayed_start(**kwargs):
    """装饰器：推迟某个函数的执行"""
    return functools.partial(DelayedStart, **kwargs)

@delayed_start(duration=2)
def hello():
    print('hello world!')



'''
Wait for 2 second before starting...
hello world!
'''
hello()

'''
Call without delay
hello world!
'''
hello.eager_call()