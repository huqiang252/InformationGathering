#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/1
# 文件名称   ：validator.py



class Validator:
    """校验器基类：统一注册所有校验器类，方便后续使用"""

    _validators = {}

    def __init_subclass__(cls, **kwargs):
        print('{} registered, extra kwargs: {}'.format(cls.__name__, kwargs))
        Validator._validators[cls.__name__] = cls


class StringValidator(Validator, foo='bar'):
    name = 'string'

class IntegerValidator(Validator):
    name = 'int'

print(Validator._validators)
#StringValidator registered, extra kwargs: {'foo': 'bar'}
# IntegerValidator registered, extra kwargs: {}
# {'StringValidator': <class '__main__.StringValidator'>, 'IntegerValidator': <class '__main__.IntegerValidator'>}