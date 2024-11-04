#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/27


class AreaCalculator:
    PI = 3.14

    @classmethod
    def calculate_circle_area(cls, r):
        return cls.PI * r * r

    @staticmethod
    def calculate_rectangle_area(width, height):
        return width * height


print(AreaCalculator.calculate_circle_area(10))
print(AreaCalculator.calculate_rectangle_area(3, 5))

#314.0
# 15
