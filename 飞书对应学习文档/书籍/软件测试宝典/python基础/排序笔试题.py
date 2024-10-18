#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-10-17

##方法1
L = [1,2,3,1,2,3,58,12,54,90]
newList=[]
for i in set(L):
    newList.append([i,L.count(i)])
print(newList)  #[[1, 2], [2, 2], [3, 2], [90, 1], [12, 1], [54, 1], [58, 1]]

#排序
newList.sort(key=lambda x:x[1])
print(newList)  #[[90, 1], [12, 1], [54, 1], [58, 1], [1, 2], [2, 2], [3, 2]]


##方法2
#列表推导式
newList2 =[ [i,L.count(i)] for i in set(L)]
newList2.sort(key= lambda x:x[1])
print(newList2)



##方法3
#使用内置sorted函数，一句话实现
print(sorted([ [i,L.count(i)] for i in set(L)],key= lambda x:x[1]))