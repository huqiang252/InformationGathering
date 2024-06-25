#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-06-24
from dataclasses import dataclass,field

@dataclass
class Cat:
    name: str
    color: str
    weight: str = field(default=5)
    children: list = field(default_factory=list)
    children1: list = field(default_factory=lambda:[1,2,3])
    children2: dict = field(default_factory=lambda: {"name":"喵"})



if __name__ == '__main__':
    tom = Cat("Tom", "red")
    print(tom)  #Cat(name='Tom', color='red', weight=5, children=[], children1=[1, 2, 3], children2={'name': '喵'})
