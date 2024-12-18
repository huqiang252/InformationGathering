#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/26


d = {'foo':1,'bar':2}

print(list(d.keys())[0])  #foo

print(next(iter(d.keys()))) #foo


numbers = [3, 15, 8, 100, 21, 11,42 , 15]
#找到里面第一个可以被7整除的数字

#原始写法
for num in numbers:
    if num % 7 == 0:
        print(num)
        break

#使用itertools.dropwhile
from itertools import dropwhile
for num in dropwhile(lambda x: x % 7 != 0, numbers):
    print(num)
    break


#使用next()
print(next (i for i in numbers if i % 7 == 0))