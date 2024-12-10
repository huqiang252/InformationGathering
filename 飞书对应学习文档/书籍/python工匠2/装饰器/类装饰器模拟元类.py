#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/11/30
# 文件名称   ：类装饰器模拟元类.py

_validators={}

def register(cls):
    """装饰器：统一注册所有校验器类，方便后续使用"""
    _validators[cls.name] = cls
    return cls

@register
class StringValidator:
    name = 'string'

@register
class IntegerValidator:
    name = 'int'


#查看注册结果
#{'string': <class '__main__.StringValidator'>, 'int': <class '__main__.IntegerValidator'>}
print(_validators)