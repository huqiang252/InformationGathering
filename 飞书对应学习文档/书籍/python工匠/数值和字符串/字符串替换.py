#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/17
s = '明明是中文,却使用了英文标点.'
# 创建替换规则表：',' -> '，', '.' -> '。'
table = s.maketrans(',.', '，。')
s.translate(table)
print(s) #'明明是中文，却使用了英文标点。'
