#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-06-24
from dataclasses import dataclass,field
#如果为 True（默认值），该字段包含在生成的 repr() 方法返回的字符串中。
# 如果为 False，该字段不会包含在生成的 repr() 方法返回的字符串中。
@dataclass
class Cat:
    name: str
    color: str = field(repr=False)
    weight: str


if __name__ == '__main__':
    tom = Cat("tom", "red", 5)
    print(tom)  #Cat(name='tom', weight=5)
