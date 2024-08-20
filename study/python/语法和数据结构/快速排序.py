#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-07-28


def quickSort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # 选取数组中间元素作为基准值
    left = [x for x in arr if x < pivot]  # 小于基准值的部分放在左边列表
    middle = [x for x in arr if x == pivot]  # 等于基准值的部分放在中间列表
    right = [x for x in arr if x > pivot]  # 大于基准值的部分放在右边列表

    return quickSort(left) + middle + quickSort(right)  # 合并结果返回
