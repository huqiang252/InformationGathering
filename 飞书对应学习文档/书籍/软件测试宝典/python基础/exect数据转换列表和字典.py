#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-10-19
import pandas

path = "D:\\example.xls"
df = pandas.read_excel(path)

name,age,weight = [],[],[]

#遍历每一行数据
for i in df.index.values:
    #按行读取，并把每行内容转换字典
    row = df.loc[i].to_dict()

    name.append(row.get('name'))
    age.append(row.get('age'))
    weight.append(row.get('weight'))

print({'name':name,"age":age,'weight':weight})  #{'name': ['qwetest1', 18, 50, 'qwetest2', 19, 51, 'qwetest3', 20, 52, 'qwetest4', 21, 53, 'qwetest5', 22, 54, 'qwetest6', 23, 55, 'qwetest7', 24, 56], 'age': [], 'weight': []}
