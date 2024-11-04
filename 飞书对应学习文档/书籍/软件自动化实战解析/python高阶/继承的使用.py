#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/27


class Shape:

    def __init__(self):
        self.name = 'Shape'

    def self_introduction(self):
        print('I am a shape')

class Triangle(Shape):
    pass

shape = Shape()
shape.self_introduction()

triangle = Triangle()
triangle.self_introduction()
print(triangle.name)