#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/26

#原始写法
def sum_even_only(numbers):
    """对numbers 里面所有的偶数求和"""
    result = 0
    for num in numbers:
        if num % 2 == 0:
            result += num
    return result


# 使用生成器
def even_only_gen(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num


def sum_even_only_v2(numbers):
    """对numbers 里面所有的偶数求和"""
    result = 0
    for num in even_only_gen( numbers ):
        result += num
    return result


