#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-10-19


def love(func):
    def wrapper(*args,**kwargs):
        print('调用前-----')
        func(*args,**kwargs)
        print('调用后-----')

    return wrapper


#在函数中使用装饰器
@love
def fun():
    print('我是孤独函数')


#在类中使用装饰器

class MyMethod(object):
    @love
    def fun(self):
        print('我是类中函数')


if __name__ == '__main__':
    fun()
    print('*'*50)
    MyMethod().fun()


