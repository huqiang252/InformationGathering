#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/20


def add_list(in_func_obj):
    print(f'In add [before]: in_func_obj="{in_func_obj}"')
    in_func_obj += ['baz']
    print(f'In add [after]: in_func_obj="{in_func_obj}"')


orig_obj = ['foo', 'bar']
print(f'Outside [before]: orig_obj="{orig_obj}"')
add_list(orig_obj)
print(f'Outside [after]: orig_obj="{orig_obj}"')
#
# Outside [before]: orig_obj="['foo', 'bar']"
# In add [before]: in_func_obj="['foo', 'bar']"
# In add [after]: in_func_obj="['foo', 'bar', 'baz']"
# Outside [after]: orig_obj="['foo', 'bar', 'baz']"