#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/26

#一般方法
def find_twelve(num_list1, num_list2, num_list3):
    """从3 个数字列表中，寻找是否存在和为 12 的3 个数"""
    for num1 in num_list1:
        for num2 in num_list2:
            for num3 in num_list3:
                if num1 + num2 + num3 == 12:
                    return num1, num2, num3



#使用product
from itertools import product
def find_twelve_v2(num_list1, num_list2, num_list3):
    """从3 个数字列表中，寻找是否存在和为 12 的3 个数"""
    for num1, num2, num3 in product(num_list1, num_list2, num_list3):
        if num1 + num2 + num3 == 12:
            return num1, num2, num3