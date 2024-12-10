#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/2
# 文件名称   ：duckwithSomthing.py


class DuckWithProperty:
    @property
    def color(self):
        return 'gray'
class DuckWithStaticMethod:
    @staticmethod
    def color(self):
        return 'gray'


if __name__ == '__main__':

    d_static = DuckWithStaticMethod()
    d_static.color='blue'
    print(d_static.color) #blue

    d = DuckWithProperty()
    d.color='yellow'  #AttributeError: can't set attribute

