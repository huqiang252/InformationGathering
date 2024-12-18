#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/22
from collections import defaultdict

init_dict = defaultdict(int)
print(init_dict) #defaultdict(<class 'int'>, {})

init_dict['foo']+=1

print(init_dict) #defaultdict(<class 'int'>, {'foo': 1})
print(dict(init_dict)) #{'foo': 1}