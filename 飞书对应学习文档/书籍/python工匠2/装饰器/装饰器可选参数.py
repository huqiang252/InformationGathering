#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/11/30
# 文件名称   ：装饰器可选参数.PY

import time
def delayed_start(func=None, *, duration=1):
    """装饰器：在执行被装饰函数前，等待一段时间

    :param duration: 需要等待的秒数
    """

    def decorator(_func):
        def wrapper(*args, **kwargs):
            print(f'Wait for {duration} second before starting...')
            time.sleep(duration)
            return _func(*args, **kwargs)

        return wrapper
    if func is None:
        return decorator
    else:
        return decorator(func)



@delayed_start(duration=2)
def hello():
    '''欢迎你'''
    print('hello world')


hello()


