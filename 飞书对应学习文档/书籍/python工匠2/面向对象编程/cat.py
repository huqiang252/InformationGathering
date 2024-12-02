#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/11/30
# 文件名称   ：cat.py

import random
class Cat:
    def __init__(self,name):
        self.name = name

    def say(self):
        sound = self.get_sound()
        print(f'{self.name}:{sound}')

    @staticmethod
    def get_sound():
        repeats = random.randrange(1,10)
        return ' '.join(['Meow']*repeats)


if __name__ == '__main__':
    c = Cat('Tom')
    c.say()  #Tom:Meow Meow Meow Meow

    print(Cat.get_sound())  #Meow Meow Meow Meow Meow

