#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/9
import logging
class TerminalCmd():
    """终端命令"""

    def __init__(self, text):
        self.__cmdName = "ls"
        self.__cmdArgs = ['-al']


class Person():
    """人"""
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

if __name__ == '__main__':
    terObj=TerminalCmd( 'ls -al' )
    print(terObj.__dict__)  #{'_TerminalCmd__cmdName': 'ls', '_TerminalCmd__cmdArgs': ['-al']}


    personObj = Person("张三", 18, 60, 170)
    print(personObj.__dict__) #{'name': '张三', 'age': 18, 'weight': 60, 'height': 170}
