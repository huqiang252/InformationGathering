#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/11/30
# 文件名称   ：类可调用对象.PY


class Foo:
    def __call__(self,name):
        print(f'Hello,{name}')


foo = Foo()
print(callable(foo))  #True

#调用类实例时，可以像普通函数一样提供额外参数
foo('qiang') #Hello,qiang
