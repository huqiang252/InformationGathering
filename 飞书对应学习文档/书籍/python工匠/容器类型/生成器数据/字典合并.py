#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/24

d1 = {'name':'apple'}
d2 = {'name':'banana','price':10}
print(d1|d2) #{'name': 'banana', 'price': 10}
print(d2|d1)  #{'name': 'apple', 'price': 10}