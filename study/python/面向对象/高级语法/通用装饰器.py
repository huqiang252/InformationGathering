#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-07-27
# 做为装饰器名的外函数，使用参数接收被装饰函数的引用
def decorator(func):
    # 内函数的可变参数用来接收被装饰函数使用的参数
    def inner(*args, **kwargs):
        # 装饰器功能代码
        # 调用被装饰函数，并将接收的参数传递给被装饰函数，保存被装饰函数执行结果
        result = func(*args, **kwargs)
        # 返回被装饰函数执行结果
        return result
    # 返回内函数引用
    return inner

