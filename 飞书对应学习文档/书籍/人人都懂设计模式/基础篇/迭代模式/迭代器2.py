#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/7
def fibonacci(maxNum):
    """斐波那契数列的生成器"""
    a = b = 1
    for i in range(maxNum):
        yield a
        a, b = b, a + b


print("将Iterable对象转成Iterator对象：")
l = [1, 2, 3]
itrL = iter(l)
print(next(itrL))
print(next(itrL))
print(next(itrL))

print("next()函数遍历迭代器元素：")
fib = fibonacci(4)
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))