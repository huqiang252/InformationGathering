#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-06-24
'''

使用 dataclass 之前需要使用 from dataclasses import dataclass 进行导入，然后以装饰器的形式进行使用。
默认情况下，@dataclass 装饰器会生成 __repr__、 __init__ 、 __eq__ 三个方法

'''



from dataclasses import dataclass



@dataclass
class Student:
    name: str
    age: int
    gender: str

if __name__ == '__main__':
    tom1 = Student("tom", 22, "male")
    print(tom1)
    tom2 = Student("Tom", 22, "male")
    print(tom2)
    print(tom1 == tom2)
