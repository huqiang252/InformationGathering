#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/27


from datetime import date

class Student:
    def __init__(self, name):
        self.name = name
        self._birth_year = date.today().year - 6  #把成员变量变成私有

    @property
    def birth_year(self):
        return self._birth_year
