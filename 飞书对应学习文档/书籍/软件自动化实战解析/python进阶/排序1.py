#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/22


names = ['James', 'Antetokounmpo', 'Doncic']
names.sort()
print(names)  #默认按照字母排序  ['Antetokounmpo', 'Doncic', 'James']

names.sort(key=len)
print(names)  #['James', 'Doncic', 'Antetokounmpo']
names.sort(key=len,reverse=True)
print(names) #['Antetokounmpo', 'Doncic', 'James']
