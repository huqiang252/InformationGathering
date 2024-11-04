#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/2
from abc import ABCMeta,abstractmethod


class Animal(metaclass=ABCMeta):
    def __init__(self, name):
        self._name = name


    def eat(self,food):
        if (self.checkFood(food)):
            print("{} 能吃 {}".format(self._name,food.getName()))
        else:
            print("{} 不能吃 {}".format(self._name,food.getName()))

    @  abstractmethod
    def checkFood(self,food):
        #检查哪个食物能吃
        pass


class Food(metaclass=ABCMeta):
    def __init__(self,name):
        self._name = name

    def getName(self):
        return self._name

    def category(self):
        #食物分类
        pass

    def nutrient(self):
         #食物营养
        pass



class Dog(Animal):
    def __init__(self):
         super().__init__("狗")

    def checkFood(self,food):
         return food.category() == "肉类"


class Swallow(Animal):
    #燕子
    def __init__(self):
        super().__init__( "燕子" )

    def checkFood(self,food):
         return food.category() == "昆虫"



class Meat(Food):
    def __init__(self):
        super().__init__( "肉" )


    def category(self):
         return "肉类"

    def nutrient(self):
        return '蛋白质，脂肪'

class Worm(Food):
    def __init__(self):
        super().__init__( "虫" )


    def category(self):
         return "昆虫"

    def nutrient(self):
        return '蛋白质，脂肪'





if __name__ == '__main__':
    dog = Dog()
    dog.eat(Meat())
    dog.eat(Worm())

    swallow = Swallow()
    swallow.eat(Meat())
    swallow.eat(Worm())





