#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/29


class OuterSpace:
    class __InnerSpace:
        def __init__(self):
            print("I am inner space")

        def greet(self):
            print("Hello from inner space")

    __inner_space_instance = None

    def __new__(cls):
        if not OuterSpace.__inner_space_instance:
            OuterSpace.__inner_space_instance = OuterSpace.__InnerSpace()

        return OuterSpace.__inner_space_instance

space = OuterSpace()  #I am inner space
space.greet()  #Hello from inner space
