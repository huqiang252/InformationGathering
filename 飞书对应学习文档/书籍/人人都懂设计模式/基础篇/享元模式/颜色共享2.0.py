#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/9


from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法

class Flyweight(metaclass=ABCMeta):
    """享元类"""

    @abstractmethod
    def operation(self, extrinsicState):
        pass

class FlyweightImpl(Flyweight):
    """享元类的具体实现类"""

    def __init__(self, color):
        self.__color = color

    def operation(self, extrinsicState):
        # print("%s 取得 %s色颜料" % (extrinsicState, self.__color))
        print(f'{extrinsicState} 取得 {self.__color}色颜料')

class FlyweightFactory:
    """享元工厂"""

    def __init__(self):
        self.__flyweights = {}

    def getFlyweight(self, key):
        pigment = self.__flyweights.get(key)
        if pigment is None:
            pigment = FlyweightImpl(key)
        return pigment


if __name__ == '__main__':
    factory = FlyweightFactory()
    pigmentRed = factory.getFlyweight("红")
    pigmentRed.operation("梦之队")
    pigmentRed2 = factory.getFlyweight("红")
    pigmentRed2.operation("和平队")
    pigmentYellow = factory.getFlyweight("黄")
    pigmentYellow.operation("梦之队")
    pigmentBlue1 = factory.getFlyweight("蓝")
    pigmentBlue1.operation("梦之队")