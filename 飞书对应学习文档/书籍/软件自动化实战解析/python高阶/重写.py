#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/27


class Parent:
    def __init__(self, name):
        self.name = name

    def swim(self, posture):
        if posture != 'Dog paddle':
            print(self.name + ': ' + posture + ' is too hard...')
        else:
            print(self.name + ': ' + 'Dog paddle')

class Child(Parent):
    def swim(self, posture):
        print(self.name + ': ' + posture)

family = [Parent('Dad'), Child('Son'), Child('Daughter')]

for member in family:
    member.swim('Dragonfly stroke')