#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/7
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法

class Component(metaclass=ABCMeta):
    """组件"""

    def __init__(self, name):
        self._name = name

    def getName(self):
        return self._name

    def isComposite(self):
        return False

    @abstractmethod
    def feature(self, indent):
        # indent 仅用于内容输出时的缩进
        pass

class Composite(Component):
    """复合组件"""

    def __init__(self, name):
        super().__init__(name)
        self._components = []

    def addComponent(self, component):
        self._components.append(component)

    def removeComponent(self, component):
        self._components.remove(component)

    def isComposite(self):
        return True

    def feature(self, indent):
        indent += "\t"
        for component in self._components:
            print(indent, end="")
            component.feature(indent)






