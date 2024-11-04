#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/27


class Person:

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def __sleep(self):
        print("I am sleeping")


person = Person("Guido van Rossum", 50)
person._Person__sleep() #我们在私有成员名前面加上下划线和类名，就可以访问相关的私有成员