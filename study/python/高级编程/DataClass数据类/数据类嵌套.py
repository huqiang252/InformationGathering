#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-06-24
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    gender: str

@dataclass
class Class:
    name: str
    member: list[Student]


if __name__ == '__main__':
    tom = Student("Tom", 22, "male")
    jack = Student("Jack", 22, "male")
    p1 = Class("Pthon1", [tom, jack])
    print(p1)
