#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/1
# 文件名称   ：validatorSimple.py


from abc import ABC,abstractmethod
class Validator(ABC):
    """校验器抽象类"""
    @classmethod
    def __subclasshook__(cls, C):
        """任何提供了validate 方法的类，都被当作 Validator 的子类"""
        if any("validate" in B.__dict__ for B in C.__mro__):
            return True
        return NotImplemented

    @abstractmethod
    def validate(self, value):
        raise NotImplementedError

class StringValidator:
    def validate(self, value):
        ...

class Foo:
    pass


if __name__ == '__main__':
    Validator.register(Foo)
    print(isinstance(Foo(), Validator))
    print(Foo())