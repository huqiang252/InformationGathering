#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/24

import random
class DummyContext:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        # __enter__会在进入管理器时被调用，同时可以返回结果
        # 这个结果可以通过 as 关键字被调用方获取
        #
        # 此处返回一个增加了随机后缀的name
        return f'{self.name}-{random.random()}'

    def __exit__(self, exc_type, exc_val, exc_tb):
        # __exit__会在退出管理器时被调用
        print('Exiting DummyContext')
        return False

if __name__ == '__main__':
    with DummyContext('test') as name:
        print(f'Name:{name}')

# Name:test-0.9905400775955233
# Exiting DummyContext