#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/27

class Student:
    def __init__(self, id, name, major):
        self.id = id
        self.name = name
        self.major = major

    def __str__(self):
        return '#' + str(self.id) + ', ' + self.name

student = Student(1, 'Ava', 'Art')
print(student)