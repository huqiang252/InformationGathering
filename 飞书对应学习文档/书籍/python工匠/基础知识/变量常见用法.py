#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/16


attrs = [1,['piglei',100]]
user_id,(username,score) = attrs
print(user_id)
print(username) #piglei



data = ['piglei','apple','orange','banana',100]
username,*fruits,score = data
print(username)
print(fruits)  #['apple', 'orange', 'banana']
print(score) #100



for username,score in [['piglei',100],['jack',90],['tom',80]]:
    print(username)

