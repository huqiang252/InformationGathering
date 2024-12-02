#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/11/30
# 文件名称   ：递归使用.PY

from functools import lru_cache
@lru_cache
def fib(n):
    if n<2:
        return n
    return fib(n-1)+fib(n-2)


def fib_loop(n):
    a,b=0,1
    for i in  range(n):
        a,b=b,a+b
    return a
print(fib_loop(1000))
# print( [fib(i) for i in range(10)] )  #[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]