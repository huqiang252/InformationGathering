#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/27




def formal_greeting(name):
    regards = 'Best regards!'
    print('Dear {}, nice to meet you!\r\n{}'.format(name, regards))

def casual_greeting(name):
    print('Hi {}'.format(name))

def greet(greeting_function, name):
    greeting_function(name)

greet(formal_greeting, 'Ema')
greet(casual_greeting, 'Ava')