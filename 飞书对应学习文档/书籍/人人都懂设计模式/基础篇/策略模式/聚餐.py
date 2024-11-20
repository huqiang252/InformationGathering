#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/8


from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法

class IVehicle(metaclass=ABCMeta):
    """交通工具的抽象类"""

    @abstractmethod
    def running(self):
        pass


class SharedBicycle(IVehicle):
    """共享单车"""

    def running(self):
        print("骑共享单车(轻快便捷)", end='')


class ExpressBus(IVehicle):
    """快速公交"""

    def running(self):
        print("坐快速公交(经济绿色)", end='')

class Express(IVehicle):
    """快车"""

    def running(self):
        print("打快车(快速方便)", end='')


class Subway(IVehicle):
    """地铁"""

    def running(self):
        print("坐地铁(高效安全)", end='')


class Classmate:
    """参加聚餐的同学"""

    def __init__(self, name, vechicle):
        self.__name = name
        self.__vechicle = vechicle

    def attendTheDinner(self):
        print(self.__name + " ", end='')
        self.__vechicle.running()
        print(" 来参加聚餐！")


if __name__ == '__main__':
    Classmate("小明", SharedBicycle()).attendTheDinner()
    Classmate("小红", Subway()).attendTheDinner()
    Classmate("小刚", ExpressBus()).attendTheDinner()
    Classmate("小李", Express()).attendTheDinner()


