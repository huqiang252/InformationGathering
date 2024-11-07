#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/4


class InteractiveObject:
    """进行交互的对象"""
    pass

class InteractiveObjectImplA:
    """实现类A"""
    pass

class InteractiveObjectImplB:
    """实现类B"""
    pass

class Meditor:
    """中介类"""

    def __init__(self):
        self.__interactiveObjA = InteractiveObjectImplA()
        self.__interactiveObjB = InteractiveObjectImplB()

    def interative(self):
        """进行交互的操作"""
        # 通过self.__interactiveObjA和self.__interactiveObjB完成相应的交互操作
        pass