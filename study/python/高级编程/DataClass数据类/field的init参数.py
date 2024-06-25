#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-06-24
from dataclasses import dataclass,field

'''
如果为 True（默认值），该字段作为参数包含在生成的 init() 方法中。
如果为 False，该字段不会包含 init() 方法参数中。
设置为不初始化的属性，在打印实例对象时会报错，解决方法有两种
在指定 init为 False 的同时指定 repr 也为 False
在使用对象信息之前，对未初始化的属性进行赋值
'''

#方式1
@dataclass
class Cat:
    name: str
    color: str = field(init=False, repr=False)
    weight: str


if __name__ == '__main__':
    tom = Cat("tom", 5)
    print(tom)


#方式2
# @dataclass
# class Cat:
#     name: str
#     color: str = field(init=False)
#     weight: str
#
#
# if __name__ == '__main__':
#     tom = Cat("tom", 5)
#     tom.color = "red"
#     print(tom)

