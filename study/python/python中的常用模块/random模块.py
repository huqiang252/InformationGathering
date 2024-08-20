#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-07-28


import random

print(random.random())
print(random.randint(1,10))
print(random.uniform(2,5))  #random.uniform(a,b)：生成一个 [a,b] 范围内的随机浮点数。
fruits = ["苹果", "香蕉", "樱桃"]
random_fruit = random.choice(fruits)   #random.choice(seq)：从序列 seq 中随机选择一个元素。seq 是自定义的序列。
print(random_fruit)

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)   #random.shuffle(lst)：随机打乱列表 lst 的元素顺序。


print(numbers)