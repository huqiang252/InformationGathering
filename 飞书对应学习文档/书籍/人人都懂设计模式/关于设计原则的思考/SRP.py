#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/2
# # First method
class Animal:
    """动物"""

    def __init__(self, name, type):
        self.__name = name
        self.__type = type

    def running(self):
        if(self.__type == "水生"):
            print(self.__name + "在水里游...")
        else:
            print(self.__name + "在陆上跑...")


Animal("狗", "陆生").running()
Animal("鱼", "水生").running()


# Second method
class Animal:
    """动物"""

    def __init__(self, name):
        self.__name = name

    def running(self):
        print(self.__name + "在陆上跑...")

    def swimming(self):
        print(self.__name + "在水里游...")


Animal("狗").running()
Animal("鱼").swimming()