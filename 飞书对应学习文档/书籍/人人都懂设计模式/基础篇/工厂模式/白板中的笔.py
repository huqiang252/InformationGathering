#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/8


from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法
from enum import Enum
# Python3.4 之后支持枚举Enum的语法

class PenType(Enum):
    """画笔类型"""
    PenTypeLine = 1
    PenTypeRect = 2
    PenTypeEllipse = 3


class Pen(metaclass=ABCMeta):
    """画笔"""

    def __init__(self, name):
        self.__name = name

    @abstractmethod
    def getType(self):
        pass

    def getName(self):
        return self.__name


class LinePen(Pen):
    """直线画笔"""

    def __init__(self, name):
        super().__init__(name)

    def getType(self):
        return PenType.PenTypeLine

class RectanglePen(Pen):
    """矩形画笔"""

    def __init__(self, name):
        super().__init__(name)

    def getType(self):
        return PenType.PenTypeRect


class EllipsePen(Pen):
    """椭圆画笔"""

    def __init__(self, name):
        super().__init__(name)

    def getType(self):
        return PenType.PenTypeEllipse


class PenFactory:
    """画笔工厂类"""

    def __init__(self):
        "定义一个字典(key:PenType，value：Pen)来存放对象,确保每一个类型只会有一个对象"
        self.__pens = {}

    def getSingleObj(self, penType, name):
        """获得唯一实例的对象"""


    def createPen(self, penType):
        """创建画笔"""
        if (self.__pens.get(penType) is None):
            # 如果该对象不存在，则创建一个对象并存到字典中
            # print(f'penType={penType}')
            if penType == PenType.PenTypeLine:
                pen = LinePen("直线画笔")
            elif penType == PenType.PenTypeRect:
                pen = RectanglePen("矩形画笔")
            elif penType == PenType.PenTypeEllipse:
                pen = EllipsePen("椭圆画笔")
            else:
                pen = Pen("")
            self.__pens[penType] = pen
        # 否则直接返回字典中的对象
        return self.__pens[penType]


if __name__ == '__main__':
    factory = PenFactory()
    linePen = factory.createPen( PenType.PenTypeLine )
    print( "创建了 %s，对象id：%s， 类型：%s" % (linePen.getName(), id( linePen ), linePen.getType()) )
    rectPen = factory.createPen( PenType.PenTypeRect )
    print( "创建了 %s，对象id：%s， 类型：%s" % (rectPen.getName(), id( rectPen ), rectPen.getType()) )
    rectPen2 = factory.createPen( PenType.PenTypeRect )
    print( "创建了 %s，对象id：%s， 类型：%s" % (rectPen2.getName(), id( rectPen2 ), rectPen2.getType()) )
    ellipsePen = factory.createPen( PenType.PenTypeEllipse )
    print( "创建了 %s，对象id：%s， 类型：%s" % (ellipsePen.getName(), id( ellipsePen ), ellipsePen.getType()) )

