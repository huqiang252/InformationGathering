#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/17

username, score = 'piglei', 100
# 1. C 语言风格格式化
print('Welcome %s, your score is %d' % (username, score))
# 2. str.format
print('Welcome {}, your score is {:d}'.format(username, score))
# 3. f-string，最短最直观
print(f'Welcome {username}, your score is {score:d}')
# 输出：
# Welcome piglei, your score is 100



#将 username靠右对齐，左侧补空格到一共 20个字符
# 以下两种方式将输出同样的内容
print('{:>20}'.format(username))
print(f'{username:>20}')
# 输出：
#               piglei


#使用str.format支持位置参数来格式化字符串，可以很好支持参数的重复使用
print('{0}: name={0} score={1}'.format(username, score))
# 输出：
# piglei: name=piglei score=100
