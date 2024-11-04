#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/27


from datetime import date

class Student:
    def __init__(self, name):
        self.name = name
        self._birth_year = date.today().year - 6

    @property
    def birth_year(self):
        return self._birth_year

    @birth_year.setter
    def birth_year(self, new_year):
        if new_year > date.today().year:
            print("Too young as a student!!")
            return

        self._birth_year = new_year

student1 = Student('Zhang')
print(student1.birth_year)

student1.birth_year = 2019
print(student1.birth_year)

student1.birth_year = 2070
print(student1.birth_year)