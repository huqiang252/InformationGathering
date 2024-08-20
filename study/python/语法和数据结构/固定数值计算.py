#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-07-28


def case_2():
    nums = [12,34,3,6,56,33434,6,3,23,23,23,57,78,11,1,8,9]
    sum = 0
    avg = None
    max_num = nums[0]
    min_num = nums[0]

    for n in nums:
        sum += n
        if n > max_num:
            max_num = n

        if n < min_num:
            min_num = n

    print("SUM:", sum)
    avg = sum / len(nums)
    print("AVG:", avg)
    print("MAX:", max_num)
    print("MIN:", min_num)
