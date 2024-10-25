#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/25


numbers = [3, 15, 8, 100, 7, 11, 66, 15]

index = 0
while index < len(numbers):
    number = numbers[index]
    if number % 2 != 0:
        del(numbers[index])
    else:
        index += 1

print(numbers)