#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/2
# 文件名称   ：person.py


class Person:
    def __init__(self, name: str, age):
        self.name = name
        self.age = age  #这个必须用self.age  触发setter方法进行校验

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        '''设置年龄，只允许0-150之间的数值'''
        try:
            value=int(value)
        except (TypeError,ValueError):
            raise ValueError(f"年龄必须为整数!")

        if not (0 < value < 150):
            raise ValueError(f"年龄必须为0-150之间的整数!")
        self._age=value


    def __repr__(self):
        return f"Person(name={self.name}, age={self._age})"

if __name__ == '__main__':
    p = Person("小王", '80')
    # p = Person("小王", 'sdfa') #ValueError: 年龄必须为整数!
    p = Person("小王", -20) #ValueError: 年龄必须为0-150之间的整数!