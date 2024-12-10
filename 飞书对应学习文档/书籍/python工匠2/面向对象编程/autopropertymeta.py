#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/1
# 文件名称   ：autopropertymeta.py


import time
import types
class AutoPropertyMeta(type):
    """元类：
    - 把所有类方法变成动态属性
    - 为所有实例增加创建时间属性
    """
    def __new__(cls, name, bases, attrs):
        for key, value in attrs.items():
            if isinstance(value, types.FunctionType) and not key.startswith('_'):
               attrs[key] = property(value)
        return super().__new__(cls, name, bases, attrs)
    def __call__(cls, *args, **kwargs):
        inst = super().__call__(*args, **kwargs)
        inst.created_at = time.time()
        return inst



import random
class Cat(metaclass=AutoPropertyMeta):
    def __init__(self, name):
        self.name = name
    def sound(self):
        repeats = random.randrange(1,10)
        return ' '.join(['Meow']*repeats)


if __name__ == '__main__':
    milo = Cat('Milo')
    print(milo.sound)  #sound原本是方法，但是被元类自动转换成属性了
    print(milo.created_at)  #读取元类定义的创建时间

#Meow Meow Meow Meow Meow Meow Meow Meow Meow
#1733020616.7035217
