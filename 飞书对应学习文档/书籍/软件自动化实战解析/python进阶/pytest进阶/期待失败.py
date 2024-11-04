#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/27

import pytest

PI = 3.14

def calculate_perimeter(r):
    if not isinstance(r, int):
        raise TypeError('Accept integer radius only for calculating perimeter')

    if r < 0:
        raise ValueError('Radius cannot be negative')

    return 2 * PI * r

@pytest.mark.xfail(raises=TypeError, reason="Any type other than int is illegal")
def test_perimeter_calculator_by_str_input():
    calculate_perimeter('12')

@pytest.mark.xfail(raises=ValueError, reason="Radius cannot be negative")
def test_perimeter_calculator_by_negative_integer():
    calculate_perimeter(-1)


@pytest.mark.xfail(reason="BUG-12345 waiting to be fixed")
def test_perimeter_calculator_by_positive_integer():
    actual = calculate_perimeter(1)
    expected = 6.28
    assert actual == expected, 'Radius of positive integer is supported'

#执行后：======================== 2 xfailed, 1 xpassed in 0.11s ========================

