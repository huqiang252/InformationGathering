#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/26


# def dump_value(value, extra=None):
#     if extra is None:
#         # 无法区分是否提供 None 是不是主动传入
#         ...
# # 两种调用方式
#
# value = 123
# dump_value(value)
# dump_value(value, extra=None)



#定义标记变量
# object 通常不会单独使用，但是拿来做这种标记变量刚刚好
_not_set = object()
def dump_value(value, extra=_not_set):
    if extra is _not_set:
        # 调用方没有传递 extra 参数
        print(f'运行value:{value}')
    else:
        print(f'运行value:{value},extra:{extra}')

value ="ljj"
dump_value(value) #运行value:ljj
dump_value(value, extra=None) #运行value:ljj,extra:None