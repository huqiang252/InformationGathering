#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/20


from collections import  namedtuple

#除了用逗号来分隔具名元组的字段名称以外，还可以用空格分隔：'width height'，或是直接使用一个字符串列表:['width', 'height']
Rectangle = namedtuple('Rectangle','width,height')

# rect = Rectangle(100,20)
rect = Rectangle(width=100,height=20)

print(rect[1]) #20
print(rect.height) #20

from typing import NamedTuple
class Rectangle(NamedTuple):
    width: int
    height: int

rect = Rectangle(100,20)
#提供错误的类型来初始化
rect_wrong_type = Rectangle('string', 'not_a_number')
print(rect_wrong_type.height)  #not_a_number
