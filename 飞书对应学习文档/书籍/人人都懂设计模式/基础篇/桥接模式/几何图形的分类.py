#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/10
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法

class Shape(metaclass=ABCMeta):
    """形状"""

    def __init__(self, color):
        self._color = color

    @abstractmethod
    def getShapeType(self):
        pass

    def getShapeInfo(self):
        return self._color.getColor() + "的" + self.getShapeType()


class Rectange(Shape):
    """矩形"""

    def __init__(self, color):
        super().__init__(color)

    def getShapeType(self):
        return "矩形"

class Ellipse(Shape):
    """椭圆"""

    def __init__(self, color):
        super().__init__(color)

    def getShapeType(self):
        return "椭圆"

class Color(metaclass=ABCMeta):
    """颜色"""

    @abstractmethod
    def getColor(self):
        pass


class Red(Color):
    """红色"""

    def getColor(self):
        return "红色"


class Green(Color):
    """绿色"""

    def getColor(self):
        return "绿色"


if __name__ == '__main__':
    redRect = Rectange(Red())
    print(redRect.getShapeInfo())

    greenRect = Rectange(Green())
    print(greenRect.getShapeInfo())

    redEllipse = Ellipse(Red())
    print(redEllipse.getShapeInfo())

    greenEllipse = Ellipse(Green())
    print(greenEllipse.getShapeInfo())