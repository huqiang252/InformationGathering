#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/22


import functools
#想根据每个字符串元素的最后一个字母进行排序。
def last_char_comparator(item1, item2):
    if item1[-1] > item2[-1]:
        return 1

    if item1[-1] < item2[-1]:
        return -1

    return 0

names = ['Antetokounmpo', 'Wiggins', 'Doncic', 'James']
names.sort(key=functools.cmp_to_key(last_char_comparator))
print(names) #['Doncic', 'Antetokounmpo', 'Wiggins', 'James']
