#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/3

from abc import ABCMeta,abstractmethod

class Observer(metaclass=ABCMeta):
    #观察者的基类
    @abstractmethod
    def update(self,observable,object):
        pass

class Observable:
    #被观察者的基类
    def __init__(self):
        self.__observers = []

    def addObserver(self,observer):
        self.__observers.append(observer)

    def removeObserver(self,observer):
        self.__observers.remove(observer)

    def notifyObservers(self,object=None):
        for observer in self.__observers:
            observer.update(self,object)