#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/1
# 文件名称   ：infodumpermixin.py



class InfoDumperMixin:
    """Mixin：输出当前实例信息"""
    def dump_info(self):
        d = self.__dict__
        print("Number of members: {}".format(len(d)))
        print("Details:")
        for key, value in d.items():
            print(f' - {key}: {value}')


class Person(InfoDumperMixin):
    """人"""
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    p = Person('Tom', 18)
    p.dump_info()

#输出
# Number of members: 2
# Details:
#  - name: Tom
#  - age: 18
