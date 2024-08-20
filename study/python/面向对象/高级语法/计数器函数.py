#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-07-28


# 定义装饰器函数
def count_calls(func):
    count = 0  # 初始化计数器变量

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"函数 '{func.__name__}' 已被调用 {count} 次。")
        return func(*args, **kwargs)  # 调用原始函数

    return wrapper


# 使用装饰器来计数函数调用
@count_calls
def greet(name):
    return f"Hello, {name}!"


# 调用被装饰的函数
print(greet("Alice"))
print(greet("Bob"))
print(greet("Charlie"))
