#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/1
# 文件名称   ：多重继承.py


class A:
    def say(self):
        print("I'm A")

class B(A):
    pass

class C(A):
    def say(self):
        print("I'm C")

class D(B, C):
    pass


if __name__ == '__main__':
    print(D.mro())  #[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

    D().say()  #I'm C
