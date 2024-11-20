#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/7
from collections.abc import Iterable,Iterator

#  方法一：使用()定义生成器
gen = (x * x for x in range(10))

#  方法二：使用yield定义generator函数
def fibonacci(maxNum):
    """斐波那契数列的生成器"""
    a = b = 1
    for i in range(maxNum):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    print( "方法一，0-9的平方数：" )
    for e in gen:
        print( e, end="\t" )
    print()

    print( "方法二，斐波那契数列：" )
    fib = fibonacci( 10 )
    for n in fib:
        print( n, end="\t" )
    print()

    print( "内置容器的for循环：" )
    arr = [x * x for x in range( 10 )]
    for e in arr:
        print( e, end="\t" )
    print()

    print()
    print( type( gen ) )
    print( type( fib ) )
    print( type( arr ) )

    print( "是否为Iterable对象：" )
    print( isinstance( [], Iterable ) )  #True
    print( isinstance( {}, Iterable ) ) #True
    print( isinstance( (1, 2, 3), Iterable ) ) #True
    print( isinstance( set( [1, 2, 3] ), Iterable ) ) #True
    print( isinstance( "string", Iterable ) ) #True
    print( isinstance( gen, Iterable ) ) #True
    print( isinstance( fibonacci( 10 ), Iterable ) ) #True
    print( "是否为Iterator对象：" )
    print( isinstance( [], Iterator ) )  #False
    print( isinstance( {}, Iterator ) ) #False
    print( isinstance( (1, 2, 3), Iterator ) ) #False
    print( isinstance( set( [1, 2, 3] ), Iterator ) ) #False
    print( isinstance( "string", Iterator ) ) #False
    print( isinstance( gen, Iterator ) ) #True
    print( isinstance( fibonacci( 10 ), Iterator ) ) #True
