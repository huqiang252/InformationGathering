#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/27


class Student:

    min_age = 16
    total_count = 0

    def __init__(self, name):
        self.student_id = None
        self.name = name
        Student.total_count += 1

print(Student.total_count) #0

Student('student1')
print(Student.total_count) #1

Student('student2')
student3 = Student('student3')

print(Student.total_count) #3
print(student3.total_count) #3


