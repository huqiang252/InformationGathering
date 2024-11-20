#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/7

from collections.abc import Iterator,Iterable
class NumberSequence:
    """生成一个间隔为step的数字系列"""

    def __init__(self, init, step, max = 100):
        self.__data = init
        self.__step = step
        self.__max = max

    def __iter__(self):
        return self

    def __next__(self):
        if(self.__data < self.__max):
            tmp = self.__data
            self.__data += self.__step
            return tmp
        else:
            raise StopIteration


if __name__ == '__main__':
    numSeq = NumberSequence( 0, 5, 20 )
    print( isinstance( numSeq, Iterable ) )
    print( isinstance( numSeq, Iterator ) )
    for n in numSeq:
        print( n, end="\t" )