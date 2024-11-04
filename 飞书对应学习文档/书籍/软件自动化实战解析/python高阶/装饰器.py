#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/27


from datetime import datetime

def function_time_logger(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print(' - Executed at {}\r\n'.format(datetime.now()))

    return wrapper

@function_time_logger
def bye():
    print('Bye bye!')

@function_time_logger
def greet(name):
    print('Hello {}!'.format(name))

greet('Ava')
bye()