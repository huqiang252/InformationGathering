#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/10


def callback(*args,**kwargs):
    '''回调函数'''
    #todo 函数体的实现
    print('回调函数')
    pass


def otherFun(fun,*args,**kwargs):
    #高阶函数，也叫包含函数
    fun(*args,**kwargs)


otherFun(callback)
