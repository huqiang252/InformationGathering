#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/9
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法

class DataNode(metaclass=ABCMeta):
    """数据结构类"""

    def accept(self, visitor):
        """接受访问者的访问"""
        visitor.visit(self)

class Visitor(metaclass=ABCMeta):
    """访问者"""

    @abstractmethod
    def visit(self, data):
        """对数据对象的访问操作"""
        pass


class ObjectStructure:
    """数据结构的管理类，也是数据对象的一个容器，可遍历容器内的所有元素"""

    def __init__(self):
        self.__datas = []

    def add(self, dataElement):
        self.__datas.append(dataElement)

    def action(self, visitor):
        """进行数据访问的操作"""
        for data in self.__datas:
            data.accept(visitor)


class Animal(DataNode):
    """动物类"""

    def __init__(self, name, isMale, age, weight):
        self.__name = name
        self.__isMale = isMale
        self.__age = age
        self.__weight = weight

    def getName(self):
        return self.__name

    def isMale(self):
        return self.__isMale

    def getAge(self):
        return self.__age

    def getWeight(self):
        return self.__weight

class Cat(Animal):
    """猫"""

    def __init__(self, name, isMale, age, weight):
        super().__init__(name, isMale, age, weight)

    def speak(self):
        print("miao~")


class Dog(Animal):
    """狗"""

    def __init__(self,  name, isMale, age, weight):
        super().__init__( name, isMale, age, weight)

    def speak(self):
        print("wang~")


class GenderCounter(Visitor):
    """性别统计"""

    def __init__(self):
        self.__maleCat = 0
        self.__femaleCat = 0
        self.__maleDog = 0
        self.__femalDog = 0

    def visit(self, data):
        if isinstance(data, Cat):
            if data.isMale():
                self.__maleCat += 1
            else:
                self.__femaleCat += 1
        elif isinstance(data, Dog):
            if data.isMale():
                self.__maleDog += 1
            else:
                self.__femalDog += 1
        else:
            print("Not support this type")

    def getInfo(self):
        print("%d只雄猫，%d只雌猫，%d只雄狗，%d只雌狗。"
              % (self.__maleCat, self.__femaleCat, self.__maleDog, self.__femalDog) )


class WeightCounter(Visitor):
    """体重的统计"""

    def __init__(self):
        self.__catNum = 0
        self.__catWeight = 0
        self.__dogNum = 0
        self.__dogWeight  = 0

    def visit(self, data):
        if isinstance(data, Cat):
            self.__catNum +=1
            self.__catWeight += data.getWeight()
        elif isinstance(data, Dog):
            self.__dogNum += 1
            self.__dogWeight += data.getWeight()
        else:
            print("Not support this type")

    def getInfo(self):
        print("猫的平均体重是：%0.2fkg， 狗的平均体重是：%0.2fkg" %
              ((self.__catWeight / self.__catNum),(self.__dogWeight / self.__dogNum)))


class AgeCounter(Visitor):
    """年龄统计"""

    def __init__(self):
        self.__catMaxAge = 0
        self.__dogMaxAge = 0

    def visit(self, data):
        if isinstance(data, Cat):
            if self.__catMaxAge < data.getAge():
                self.__catMaxAge = data.getAge()
        elif isinstance(data, Dog):
            if self.__dogMaxAge < data.getAge():
                self.__dogMaxAge = data.getAge()
        else:
            print("Not support this type")

    def getInfo(self):
        print("猫的最大年龄是：%s，狗的最大年龄是：%s" % (self.__catMaxAge, self.__dogMaxAge) )


if __name__ == '__main__':
    animals  = ObjectStructure()
    animals.add(Cat("大花猫", True, 3, 5))
    animals.add(Cat("二花猫", False, 2, 4))
    animals.add(Cat("三花猫", True, 1, 3))
    animals.add(Dog("旺财", True, 5, 15))
    animals.add(Dog("二狗", False, 4, 12))
    animals.add(Dog("三狗", True, 3, 9))
    genderCounter = GenderCounter()
    animals.action(genderCounter)
    genderCounter.getInfo()
    print()

    weightCounter=WeightCounter()
    animals.action(weightCounter)
    weightCounter.getInfo()
    print()

    ageCounter=AgeCounter()
    animals.action(ageCounter)
    ageCounter.getInfo()