#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/11/30
# 文件名称   ：duck.py


import random
class Duck:
    def __init__(self,color):
        self.color = color


    def quack(self):
        print(f"Hi,I'm a {self.color} duck!")

    @classmethod
    def create_random_duck(cls):
        color = random.choice(["yellow","white","gray"])
        return cls(color=color)


if __name__ == '__main__':
    duck = Duck.create_random_duck()
    duck.quack()
    print(duck.create_random_duck())  #<__main__.Duck object at 0x000002DF5CB0CDF0>
