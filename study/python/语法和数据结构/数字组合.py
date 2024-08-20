#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-07-28


for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            # 条件判断排除重复数字的排列
            if (i != k) and (i != j) and (j != k):
                print(i, j, k)
