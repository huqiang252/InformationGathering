#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/26


names = ['foo', 'bar', 'baz', 'qux','sf']

#第一种写法
index = 0
for name in names:
    print(index, name)
    index += 1


#第二种写法 --拥有2年python经验的人
for index, name in enumerate(names):
    print(index, name)