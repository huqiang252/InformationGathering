#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/22

points = [12, 3, -5, 7, 0, -10, 10]
points.sort()
print(points) #[-10, -5, 0, 3, 7, 10, 12]
points.sort(key=abs,reverse=False)
print(points) #到原点的距离考量排序，[0, 3, -5, 7, -10, 10, 12]
