#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/19


def add(x,y):
    return x+y


if __name__ == '__main__':
    import dis

    print( dis.dis( add) )