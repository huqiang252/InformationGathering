#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/22


points = [
    [121, 75, 140],
    [90, 149, 80],
    [120, 120, 120]
]

points.sort(key=sum)
print(points)  #[[90, 149, 80], [121, 75, 140], [120, 120, 120]]
