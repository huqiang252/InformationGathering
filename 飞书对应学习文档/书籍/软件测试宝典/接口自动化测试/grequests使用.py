#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-10-19
import gevent.monkey
gevent.monkey.patch_all(thread=False, select=False)  #grequest的猴子补丁

import time
import requests
import grequests
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
def io_requests_20():
    path = "http://www.zhiguyichuan.com"
    return [requests.get(path).text for i in range(20)]


@getTime()
def aio_requests_20():
    path = "http://www.zhiguyichuan.com"
    res = [grequests.get(path) for number in range(20)]
    resp = grequests.map(res)
    return resp

if __name__ == '__main__':
    io_requests_20()
    aio_requests_20()


