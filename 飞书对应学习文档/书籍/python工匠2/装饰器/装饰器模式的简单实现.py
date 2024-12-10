#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/11/30
# 文件名称   ：装饰器模式的简单实现.py


class Numbers:
    """一个包含多个数字的简单类"""

    def __init__(self, numbers):
        self.numbers = numbers

    def get(self):
        return self.numbers


class EvenOnlyDecorator:
    """装饰器类：过滤所有偶数"""

    def __init__(self, decorated):
        self.decorated = decorated

    def get(self):
        return [num for num in self.decorated.get() if num % 2 == 0]


class GreaterThanDecorator:
    """装饰器类：过滤大于某个数的数"""

    def __init__(self, decorated, min_value):
        self.decorated = decorated
        self.min_value = min_value

    def get(self):
        return [num for num in self.decorated.get() if num > self.min_value]


obj = Numbers([42, 12, 13, 17, 18, 41, 32])
even_obj = EvenOnlyDecorator(obj)
gt_obj = GreaterThanDecorator(even_obj, min_value=30)
print(gt_obj.get())  # [42, 32]