#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-06-24
from dataclasses import dataclass,field,asdict
@dataclass
class Cat:
    name: str
    color: str = field(init=False)
    weight: str


if __name__ == '__main__':
    tom = Cat("tom", 5)
    tom.color = "red"
    print(tom)
    tom_d = asdict(tom)
    print(tom_d)
