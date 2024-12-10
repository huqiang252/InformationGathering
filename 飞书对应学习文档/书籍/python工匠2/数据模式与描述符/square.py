#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/2
# 文件名称   ：square.py

from functools import total_ordering


@total_ordering
class Square:
    """正方形

    :param length: 边长
    """

    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.length == other.length
        return False

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.length < other.length
        return NotImplemented


if __name__ == '__main__':
    x = Square(5)
    y = Square(6)
    print(x<y) #True