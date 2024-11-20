#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/8

from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法

class Coffee(metaclass=ABCMeta):
    """咖啡"""

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    @abstractmethod
    def getTaste(self):
        pass


class LatteCaffe(Coffee):
    """拿铁咖啡"""

    def __init__(self, name):
        super().__init__(name)

    def getTaste(self):
        return "轻柔而香醇"

class MochaCoffee(Coffee):
    """摩卡咖啡"""

    def __init__(self, name):
        super().__init__(name)

    def getTaste(self):
        return "丝滑与醇厚"

class Coffeemaker:
    """咖啡机"""

    @staticmethod
    def makeCoffee(coffeeBean):
        "通过staticmethod装饰器修饰来定义一个静态方法"
        if(coffeeBean == "拿铁咖啡豆"):
            coffee = LatteCaffe("拿铁咖啡")
        elif(coffeeBean == "摩卡咖啡豆"):
            coffee = MochaCoffee("摩卡咖啡")
        else:
            raise ValueError("不支持的参数：%s" % coffeeBean)
        return coffee

if __name__ == '__main__':
    latte = Coffeemaker.makeCoffee( "拿铁咖啡豆" )
    print( "%s已为您准备好了，口感：%s。请慢慢享用！" % (latte.getName(), latte.getTaste()) )
    mocha = Coffeemaker.makeCoffee( "摩卡咖啡豆" )
    print( "%s已为您准备好了，口感：%s。请慢慢享用！" % (mocha.getName(), mocha.getTaste()) )
