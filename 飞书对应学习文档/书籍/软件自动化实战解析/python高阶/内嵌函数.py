#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/27


def greet(name):
    def salute(customer_name):
        print('Dear {}, nice to meet you!'.format(customer_name))

    salute(name)

greet('Ema')  #Dear Ema, nice to meet you!
