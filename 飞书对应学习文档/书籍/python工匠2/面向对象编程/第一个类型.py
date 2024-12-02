#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/11/30
# 文件名称   ：第一个类型.py


class Foo:
    def __init__(self):
        self.__bar = 'bar'



if __name__ == '__main__':
    foo = Foo()
    # print(foo.__bar)  #AttributeError: 'Foo' object has no attribute '__bar'
    print(foo._Foo__bar) #bar