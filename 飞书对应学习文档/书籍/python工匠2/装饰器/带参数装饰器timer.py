#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/11/30
# 文件名称   ：带参数装饰器timer.PY

import time
def timer(print_args=False):
    """装饰器：打印函数耗时
    :param print_args: 是否打印方法名和参数，默认为 False
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            st = time.perf_counter()
            ret = func(*args, **kwargs)
            if print_args:
                print(f'"{func.__name__}", args: {args}, kwargs: {kwargs}')
            print('time cost: {} seconds'.format(time.perf_counter() - st))
            return ret

        return wrapper

    return decorator


import random
@timer(print_args=True)
def random_sleep():
    '''随机小睡一会而'''
    time.sleep(random.random())


if __name__ == '__main__':
    random_sleep()
    #"random_sleep", args: (), kwargs: {}
    # time cost: 0.05336520000000001 seconds
    print(random_sleep.__name__)  #wrapper
    print(random_sleep.__doc__) #None
