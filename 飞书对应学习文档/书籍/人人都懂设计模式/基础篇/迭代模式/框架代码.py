#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/7

class BaseIterator:
    """迭代器"""

    def __init__(self, data):
        self.__data = data
        self.toBegin()

    def toBegin(self):
        """将指针移至起始位置"""
        self.__curIdx = -1

    def toEnd(self):
        """将指针移至结尾位置"""
        self.__curIdx = len(self.__data)

    def next(self):
        """移动至下一个元素"""
        if (self.__curIdx < len(self.__data) - 1):
            self.__curIdx += 1
            return True
        else:
            return False

    def previous(self):
        "移动至上一个元素"
        if (self.__curIdx > 0):
            self.__curIdx -= 1
            return True
        else:
            return False

    def current(self):
        """获取当前的元素"""
        return self.__data[self.__curIdx] if (self.__curIdx < len(self.__data) and self.__curIdx >= 0) else None

if __name__ == '__main__':
    print( "从前往后遍历:" )
    iterator = BaseIterator( range( 0, 10 ) )
    while (iterator.next()):
        customer = iterator.current()
        print( customer, end="\t" )
    print()

    print( "从后往前遍历:" )
    iterator.toEnd()
    while (iterator.previous()):
        customer = iterator.current()
        print( customer, end="\t" )
