#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/22

from functools import cmp_to_key

def point_comparator(item1, item2):
    total1 = item1[0]+item1[1]+item1[2]
    total2 = item2[0]+item2[1]+item2[2]

    if total1 > total2:
        return 1

    if total1 < total2:
        return -1

    return 0

points = [
    [121, 75, 140],
    [90, 149, 80],
    [120, 120, 120]
]

points.sort(key=cmp_to_key(point_comparator))
print(points)  #[[90, 149, 80], [121, 75, 140], [120, 120, 120]]
