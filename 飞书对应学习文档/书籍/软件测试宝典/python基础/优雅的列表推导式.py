#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-10-18


L = [2, 5, 6, 4, 7]

# 乘法运算
print( [i * 10 for i in L] )
# 原数和二次方根组成一个二维数组
print( [[temp, temp ** 2] for temp in L] )
# 选出大于3，再乘以3
print( [temp * 3 for temp in L if temp > 3] )
