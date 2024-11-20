#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/7

from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法

class Target(metaclass=ABCMeta):
    """目标类"""

    @abstractmethod
    def function(self):
        pass


class Adaptee:
    """源对象类"""

    def speciaficFunction(self):
        print("被适配对象的特殊功能")

class Adapter(Target):
    """适配器"""

    def __init__(self, adaptee):
        self.__adaptee = adaptee

    def function(self):
        print("进行功能的转换")
        self.__adaptee.speciaficFunction()


