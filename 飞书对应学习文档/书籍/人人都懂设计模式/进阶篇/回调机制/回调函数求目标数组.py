#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/10


def isEvenNumber(num):
    return num % 2 == 0

def isGreaterThanTen(num):
    return num > 10

def getResultNumbers(fun, elements):
    newList = []
    for item in elements:
        if (fun(item)):
            newList.append(item)
    return newList


if __name__ == '__main__':
    elements = [2,3,6,9,12,15,18]
    list1 = getResultNumbers(isEvenNumber, elements)
    list2 = getResultNumbers(isGreaterThanTen, elements)
    print("所有的偶数",list1)
    print('大于10的数',list2)