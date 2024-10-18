#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-10-18
L = [[2,5,8],[3,6,9],[1,4,7],[3,2,1]]
newList = []

for i in L:
    newList = newList+i

print(newList)  #[2, 5, 8, 3, 6, 9, 1, 4, 7, 3, 2, 1]

getList = []
for j in newList:
    if j>3 and j<8:
        getList.append(j)
print(getList)  #[5, 6, 4, 7]