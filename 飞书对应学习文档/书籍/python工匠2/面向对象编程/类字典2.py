#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/11/30
# 文件名称   ：类字典2.py

class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __setattr__(self, name, value):
        #不允许设置年龄小于0
        if name=='age' and value<0:
            raise ValueError(f"Age must be positive:{value}")
        super().__setattr__(name, value)

    def say(self):
        print(f"{self.name} {self.age} {self.sex}")


if __name__ == '__main__':
    p = Person("Tom", 18, "Male")
    p.__dict__['age']=-3 #可以突破__setattr__限制
    print(p.__dict__)  #{'name': 'Tom', 'age': -3, 'sex': 'Male'}


