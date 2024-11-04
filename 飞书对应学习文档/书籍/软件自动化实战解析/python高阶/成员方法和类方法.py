#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/27

class Student:
    min_age = 16
    total_count = 0

    @classmethod
    def next_id(cls):
        cls.total_count += 1
        return cls.total_count

    def __init__(self, name):
        self.student_id = Student.next_id()
        self.name = name


student1 = Student('Ema')  #1
print(student1.student_id)

Student('Emma')
Student('Emmma')
Student('Emmmma')
print(Student.total_count) #4