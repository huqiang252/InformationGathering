#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/24
import functools

class Student:

    def __init__(self, student_id, name, age, height):
        self.id = student_id
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return '{}: {}, {} years old, height {}'.format(self.id, self.name,
            self.age, self.height)


def student_age_sorter(student1, student2):
    if student1.age > student2.age:
        return 1

    if student1.age < student2.age:
        return -1

    return 0


students = [
    Student(1, 'Zhao', 18, 170),
    Student(5, 'Qian', 20, 160),
    Student(2, 'Sun', 19, 180),
    Student(9, 'Li', 21, 175)
]



print('Sort by age, asc')
students.sort(key=functools.cmp_to_key(student_age_sorter))
for student in students:
    print(student)

print()

print('Sort by age, des')
students.sort(key=functools.cmp_to_key(student_age_sorter), reverse=True)
for student in students:
    print(student)