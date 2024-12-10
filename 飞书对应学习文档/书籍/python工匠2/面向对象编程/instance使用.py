#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/11/30
# 文件名称   ：instance使用.py


class Validator:
    """校验器基类，校验不同种类的数据是否符合要求"""
    def validate(self, value):
        raise NotImplementedError
class NumberValidator(Validator):
    """校验输入值是否是合法数字"""
    def validate(self, value):
        ...


if __name__ == '__main__':
    print(isinstance(NumberValidator(), NumberValidator)) # True
    print(isinstance(NumberValidator(), Validator)) # True
    print(isinstance('foo',Validator)) # False