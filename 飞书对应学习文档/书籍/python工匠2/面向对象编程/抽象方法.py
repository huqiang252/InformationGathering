#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/1
# 文件名称   ：抽象方法.py
from abc import ABC,abstractmethod
class Validator(ABC):
    """校验器抽象类"""
    ...
    @abstractmethod
    def validate(self, value):
        raise NotImplementedError
class InvalidValidator(Validator):
    ...

if __name__ == '__main__':
    v = InvalidValidator()  #TypeError: Can't instantiate abstract class InvalidValidator with abstract method validate
    v.validate(1)