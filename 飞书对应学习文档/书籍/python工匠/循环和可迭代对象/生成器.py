#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/26

def range_7_gen(start, end):
    '''生成器的Range7Iterator'''
    num  = start
    while num <= end:
        if num !=0 and (num % 7 == 0 or '7' in str(num)):
            yield num
        num += 1


if __name__ == '__main__':
    nums = range_7_gen(0,20)
    print(list(num for num in nums))
    # print(next(nums)) #7
    # print(next(nums)) #14
    # print(next(nums)) #17
