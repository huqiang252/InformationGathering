#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/16
from typing import List

def magic_bubble_sort(numbers: List[int]):
    stop_position = len(numbers) - 1
    while stop_position > 0:
        for i in range(stop_position):
            previous, latter = numbers[i], numbers[i + 1]
            previous_is_even, latter_is_even = previous % 2 == 0, latter % 2 == 0
            should_swap = False

            if previous_is_even and not latter_is_even:
                should_swap = True
            elif previous_is_even == latter_is_even and previous > latter:
                should_swap = True

            if should_swap:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
        stop_position -= 1
    return numbers