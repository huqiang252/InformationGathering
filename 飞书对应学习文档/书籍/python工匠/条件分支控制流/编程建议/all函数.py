#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/24

def all_numbers_gt_10(numbers):
    '''仅当序列中所有数字大于10时，返回True'''
    if not numbers:
        return False

    for n in numbers:
        if n <= 10:
            return False

    return True


def all_numbers_gt_10_2(numbers):
    return bool(numbers) and all(n > 10 for n in numbers)