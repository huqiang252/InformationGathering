#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/2

from abc import ABCMeta,abstractmethod

class Animal(metaclass=ABCMeta):
    def __init__(self,name):
        self._name =name

    @abstractmethod
    def moving(self):
        pass


class TerrestrailAnimal(Animal):
    def __init__(self,name):
        super().__init__(name)

    def moving(self):
        print(f'{self._name}在陆地跑')



class BirdAnimal(Animal):
    def __init__(self,name):
        super().__init__(name)


    def moving(self):
        print(f'{self._name}在天上飞')


class Zoo:
    def __init__(self):
        self._animals=[]


    def addAnimal(self,animal):
        self._animals.append(animal)


    def displayActivity(self):
        print('观察每个动物的活动方式：')
        for animal in self._animals:
            animal.moving()




def testZoo():
    zoo = Zoo()
    zoo.addAnimal(TerrestrailAnimal('老虎'))
    zoo.addAnimal(BirdAnimal('老鹰'))
    zoo.displayActivity()