#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/11/30
# 文件名称   ：元类和装饰器.py



_validators = {}

class ValidatorMeta(type):
    """元类：统一注册所有校验器类，方便后续使用"""

    def __new__(cls, name, bases, attrs):
        ret = super().__new__(cls, name, bases, attrs)
        _validators[attrs['name']] = ret
        return ret


class StringValidator(metaclass=ValidatorMeta):
    name = 'string'

class IntegerValidator(metaclass=ValidatorMeta):
    name = 'int'


print(_validators)  #{'string': <class '__main__.StringValidator'>, 'int': <class '__main__.IntegerValidator'>}
