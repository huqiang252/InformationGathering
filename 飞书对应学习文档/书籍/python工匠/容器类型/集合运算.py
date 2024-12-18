#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/20

fruits_1 = {'apple', 'orange', 'pineapple'}
fruits_2 = {'tomato', 'orange', 'grapes', 'mango'}



#交集
print(fruits_1 & fruits_2) #{'orange'}

#并集
print(fruits_1 | fruits_2)  #{'orange', 'apple', 'tomato', 'grapes', 'pineapple', 'mango'}


#差集
print(fruits_1 - fruits_2)  #{'apple', 'pineapple'}