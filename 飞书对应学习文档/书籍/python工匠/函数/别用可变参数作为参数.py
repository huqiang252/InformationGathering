#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/26

def append_value(value,items=[]):
    '''向items列表追加内容，并返回列表'''
    items.append(value)
    return items

print(append_value('foo')) #['foo']
print(append_value('bar'))  #['foo', 'bar']

#通过__defaults__属性可以直接获取函数的参数默认值
print(append_value.__defaults__)  #(['foo', 'bar'],)
print(append_value.__defaults__[0].append('baz'))
print(append_value('qux')) #['foo', 'bar', 'baz', 'qux']
print(append_value.__defaults__) #(['foo', 'bar', 'baz', 'qux'],)