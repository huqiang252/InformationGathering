#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/3


from abc import ABCMeta, abstractmethod

class WaterHeater:
    def __init__(self):
        self.__observers = []
        self.__temperature = 25

    def getTeemperature(self):
        return self.__temperature

    def setTeemperature(self, temperature):
        self.__temperature = temperature
        print(f'当前温度是：{self.__temperature}C')
        self.notifies()

    def addOBserver(self, observer):
        self.__observers.append(observer)
        print(f'添加观察者：{observer.__class__}')


    def notifies(self):
        for observer in self.__observers:
            observer.update(self)


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, waterHeater):
        pass


class WashingObserver(Observer):
    def update(self, waterHeater):
        if waterHeater.getTeemperature() >= 50 and waterHeater.getTeemperature() < 70:
            print('水开了!温度正好，可以来洗澡了')


class DrinkObserver(Observer):
    def update(self, waterHeater):
        if waterHeater.getTeemperature() >= 100:
            print('水已烧开！可以来饮用了')


if __name__ == '__main__':
    waterHeater = WaterHeater()
    washObserver = WashingObserver()
    drinkObserver = DrinkObserver()
    waterHeater.addOBserver( washObserver )
    waterHeater.addOBserver( drinkObserver )
    waterHeater.setTeemperature( 60 )
    waterHeater.setTeemperature( 80 )
    waterHeater.setTeemperature( 100 )
    waterHeater.setTeemperature( 120 )
    waterHeater.setTeemperature( 70 )
    waterHeater.setTeemperature( 130 )
