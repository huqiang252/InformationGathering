#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/26

#定义函数
def add(x,y):
    return x+y
print(add(1,2))

add2 = lambda x,y:x+y #匿名函数
print(add2(1,2))


l = [13,16,21,3]
print(sorted(l,key=lambda x: x%3)) #[21, 3, 13, 16]

