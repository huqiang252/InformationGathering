#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-10-19


me = {
    "vname": "qwnetest123",
    "age": 20,
    "love": ['读书','运动'],
    'study': ['网红高中','天南大学'],
    "height": 1.75,
    'experience':[
        {'time':'2010','job':'C#开发工程师'},
        {'time':'2014','job':'资深测试工程师'}
    ]
}

#获取字典的值
print(me.values())
#获取字典的key
print(me.keys())
#获字典的每个key ,value
print(me.items())
#如果vname存在，则获取，否则设置nemd的初始值为None
print(me.setdefault('vname'))  #qwnetest123
#设置不存在的myname的初始值qqqname
print(me.setdefault('myname','qqqname'))
print(me)