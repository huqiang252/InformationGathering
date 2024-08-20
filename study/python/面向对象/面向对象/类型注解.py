#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-07-28

'''
https://python.tutorial.hogwarts.ceshiren.com/python_programming/v2/L2/tutorial/%E7%B1%BB%E5%9E%8B%E6%B3%A8%E8%A7%A3/
'''
#使用任意类型时，需要使用 typing 模块中的 Any 类型，可变数量使用 ... 表示。
from typing import Any


def show(data: tuple[Any, ...]) -> None:
    for d in data:
        print(d)


show((1, "hello", True, 123))
show((1, 2, 3))
show(('a', 'b', 'c'))




#list类型注解
def show(data: list[int]) -> None:
    for d in data:
        print(d)


show([1, 2, 3])
show(["a", 'b', 'c']) # 不符合注解类型
show([1, 2, 3, "a", 'b', 'c'])



#dict类型注解
def show(data: dict[str,int]) -> None:
    for d in data:
        print(d)


show({"a": 97})
show({"a": 97, "b": 98})
show({"c": "CC"})  # 不符合注解类型




#union类型注解，可以使用 typing 模块中的 Union 指定多个类型
from typing import Union


def show(data: Union[str,int,float,bool]) -> None:
    print(data)


show(1)
show("a")
show(3.14)
show(True)



#Sequence 类型注解
#可以使用 typing 模块中的 Sequence 指定任意可迭代类型。
from typing import Sequence

def show(data: Sequence[int]) -> None:
    print(data)


show((1,2,3))
show([1,2,3])
show("123")



#Optional 类型注解；当函数的参数有默认值，导致参数不是必须要传入的，那么你可以尝试使用 typing 模块中的Optional 来做到类型提示
from typing import Optional


def show(data: Optional[int] = 0) -> None:
    print(data)


show()
show(1)



#Callable 类型注解
#当需要表明某个函数的参数是函数时可以使用 typing 模块中的 Callable 作为类型提示。
from typing import Callable


def show(data: int) -> None:
    print(data)

def callback(func: Callable, data: int)-> None:
    func(data)

callback(show, 1)



#自定义类作为类型注解

class Person:
    pass

def show(obj: Person)->None:
    print(obj)

show(Person())
p = Person()
show(p)




