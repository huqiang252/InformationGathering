#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/23


class UpperDict(dict):
    """
    字典的键值全部大写
    """
    def __setitem__(self, k, v):
        super().__setitem__(k.upper(), v)


d = UpperDict()
d['foo']=1
print(d) #{'FOO': 1}

d.update({'bar':2})
print(d)  #{'FOO': 1, 'bar': 2}