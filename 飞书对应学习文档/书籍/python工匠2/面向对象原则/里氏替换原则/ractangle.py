#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/2
# 文件名称   ：ractangle.py


class Rectangle:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value: int):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value: int):
        self._height = value

    def get_area(self) -> int:
        """返回当前长方形的面积"""
        return self.width * self.height


class Square(Rectangle):
    """正方形

    :param length: 边长
    """

    def __init__(self, length: int):
        self._width = length
        self._height = length

    @property
    def width(self):
        return super().width

    @width.setter
    def width(self, value: int):
        self._width = value
        self._height = value

    @property
    def height(self):
        return super().height

    @height.setter
    def height(self, value: int):
        self._width = value
        self._height = value


def test_rectangle_get_area(r: Rectangle):
    r.width = 3
    r.height = 5
    assert r.get_area() == 15

if __name__ == '__main__':
    r = Rectangle(10, 20)
    print(r.get_area())
    r.width = 30
    print(r.get_area())


    s = Square(3)
    print(s.get_area())  #9

    s.height=4
    print(s.get_area()) #16