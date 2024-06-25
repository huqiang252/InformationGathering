#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-06-24



from dataclasses import dataclass


#数据在使用过程中并不想被修改，但是如果使用模型数据类实例，是不可能实现的，但是在使用 dataclass 时，可以指定 frozen=True 参数来实现该功能
@dataclass(frozen=True)
# @dataclass()
class Student:
    name: str
    age: int
    gender: str



if __name__ == '__main__':
    tom = Student("Tom", 22, "male")
    # tom.name = "tom"  # 不允许执行该行代码
    print(tom)
