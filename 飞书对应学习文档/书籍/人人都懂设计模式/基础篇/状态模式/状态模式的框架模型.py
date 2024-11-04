#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/3

from abc import ABCMeta,abstractmethod


class Context(metaclass=ABCMeta):
    #状态模式下的上下文对象
    def __init__(self):
        self.__states = []
        self.__curState = None
        self.__stateInfo = 0  #状态发生变化依赖的属性，当这一变量由多个变量共同决定时可以将其定义成一个类

    def addState(self,state):
        if state not in self.__states:
            self.__states.append(state)

    def changeState(self,state): #改变状态
        if state is None:
            return False
        if self.__curState is None:
            print(f'初始化状态为：{state.getName()} ')
        else:
            print(f'状态由{self.__curState.getName()}变为{state.getName()}')

        self.__curState=state
        self.addState(state)
        return True

    def getState(self):
        return self.__curState

    def _setStateInfo(self,stateInfo): #设置状态信息
        self.__stateInfo = stateInfo
        for state in self.__states:
            if state.isMatch(stateInfo):
                self.changeState(state)

    def _getStateInfo(self):
        return self.__stateInfo


class State(metaclass=ABCMeta):
    '''状态的基类'''
    def __init__(self,name):
        self.__name = name


    def getName(self): #获取状态名称
        return self.__name

    def isMatch(self,stateInfo): #判断状态是否匹配
        return False

    @abstractmethod
    def behavior(self,context):  #行为
        pass