#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/2
# 文件名称   ：integerField.py


class IntegerField:
    """整型字段，只允许一定范围内的整型值
    :param min_value: 允许的最小值
    :param max_value: 允许的最大值
    """
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        #将绑定属性名保存在描述符对象中
        #对于age = IntegerField(...)来说，此处的name就是"age“
        self._name = name
    def __get__(self, instance, owner=None):
        # 当不是通过实例访问时，直接返回描述符对象
        if not instance:
            return self
        # 返回保存在实例字典里的值
        return instance.__dict__[self._name]
    def __set__(self, instance, value):
        # 校验后将值保存在实例字典里
        value = self._validate_value(value)
        instance.__dict__[self._name] = value
    def _validate_value(self, value):
        """校验值是否为符合要求的整数"""
        try:
            value = int(value)
        except (TypeError, ValueError):
            raise ValueError('value is not a valid integer!')
        if not (self.min_value <= value <= self.max_value):
            raise ValueError(
                f'value must between {self.min_value} and {self.max_value}!'
            )
        return value


class Person:
    age = IntegerField(min_value=0, max_value=150)
    def __init__(self,name, age):
        self.name = name
        self.age = age

class Rectangle:
    width = IntegerField(min_value=1, max_value=10)
    height = IntegerField(min_value=1, max_value=5)
    def __init__(self,width,height):
        self.width = width
        self.height = height

if __name__ == '__main__':
    r = Rectangle(1,1)
    r.width=5
    print(r.width) #5
    print(r.height) #1 不会被更改了
    # r.width=100 #ValueError: value must between 1 and 10!

