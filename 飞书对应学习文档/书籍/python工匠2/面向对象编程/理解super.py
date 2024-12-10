#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/1
# 文件名称   ：理解super.py


class A:
    def __init__(self):
        print("I'm A")
        super().__init__()

class B(A):
    def __init__(self):
        print("I'm B")
        super().__init__()

class C(A):
    def __init__(self):
        print("I'm C")
        super().__init__()

class D1(B):
    pass

class D2(B,C):
    pass

if __name__ == '__main__':
    D2()

# 输出：
# I'm B
# I'm C
# I'm A