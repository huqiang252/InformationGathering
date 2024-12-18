#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/11/30
# 文件名称   ：timer.PY
import time
def timer(func):
    """装饰器：打印函数耗时"""

    def decorated(*args, **kwargs):
        st = time.perf_counter()
        ret = func(*args, **kwargs)
        print('time cost: {} seconds'.format(time.perf_counter() - st))
        return ret

    return decorated

import random
@timer
def random_sleep():
    '''随机小睡一会而'''
    time.sleep(random.random())


if __name__ == '__main__':
    random_sleep()  #time cost: 0.053116300000000005 seconds