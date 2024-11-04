#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/29
class OuterSpace:
    class InnerSpace:
        def __init__(self):
            print("I am inner space")

    def __init__(self):
        print("I am outer space")

outer_space = OuterSpace()
inner_space = OuterSpace.InnerSpace()

# I am outer space
# I am inner space