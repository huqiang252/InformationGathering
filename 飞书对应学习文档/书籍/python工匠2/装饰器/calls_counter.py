#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/11/30
# 文件名称   ：calls_counter.PY
import time
from functools import wraps
def timer(func):
    """装饰器：打印函数耗时"""
    @wraps(func)
    def decorated(*args, **kwargs):
        st = time.perf_counter()
        ret = func(*args, **kwargs)
        print('time cost: {} seconds'.format(time.perf_counter() - st))
        return ret

    return decorated

def calls_counter(func):
    """装饰器：记录函数被调用了多少次

    使用func.print_counter() 可以打印统计到的信息
    """
    counter = 0
    @wraps(func)
    def decorated(*args, **kwargs):
        nonlocal counter
        counter += 1
        return func(*args, **kwargs)

    def print_counter():
        print(f'Counter: {counter}')

    decorated.print_counter = print_counter #为被装饰函数增加额外函数，打印统计到的调用次数
    return decorated



import random
@timer
@calls_counter
def random_sleep():
    '''随机小睡一会而'''
    time.sleep(random.random())


if __name__ == '__main__':
    random_sleep() #time cost: 0.8236664 seconds
    random_sleep.print_counter()  #Counter: 1
    print(random_sleep.__name__)  # random_sleep
    print(random_sleep.__doc__)  # 随机小睡一会而