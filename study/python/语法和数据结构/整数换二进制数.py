#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-07-28


def func5():
    result = ""
    data = int(input("Num:"))
    while data != 0:
        tmp = data % 2
        data = data // 2
        result = str(tmp) + result
    print(result)


if __name__ == '__main__':
    func5()