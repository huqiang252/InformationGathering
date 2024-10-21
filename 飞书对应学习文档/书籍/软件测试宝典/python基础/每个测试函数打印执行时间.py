#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-10-19



import time
import functools

class getTime(object):
    def __int__(self):
        pass
    #__call__() 是一个特殊方法，它可以将一个类实列变成可调用对象
    def __call__(self,func):
        @functools.wraps(func)  #为了解决这个问题，我们通常使用内置的装饰器@functools.wrap，它会帮助保留原函数的元信息（也就是将原函数的元信息，拷贝到对应的装饰器函数里）
        def _call(*args,**kwargs):
            t1 = time.time()
            result = func(*args,**kwargs)
            print(func.__name__,f'耗费了：{time.time()-t1}')
            return result
        return _call



@getTime()
def fun():
    time.sleep(1)


class Myclass():
    @getTime()
    def funb(self):
        time.sleep(2)


if __name__ == '__main__':
    fun()
    print('*'*50)
    Myclass().funb()