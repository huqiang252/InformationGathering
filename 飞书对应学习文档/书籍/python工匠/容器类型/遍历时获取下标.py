#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/20


names = ['foo', 'bar', 'baz', 'qux','sf']

for index, name in enumerate(names):
    print(index, name)

print()

for index, name in enumerate(names, 3):
    print(index, name)