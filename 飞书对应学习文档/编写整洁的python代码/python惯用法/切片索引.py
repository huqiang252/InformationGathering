#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2025/1/11
# 文件名称   ：切片索引.py


my_numbers= (1, 1, 2, 3, 5, 8, 13, 21)
interval =  slice(1, 7, 2)
print(my_numbers[interval])   #(1, 3, 8)

interval2 = slice(None,3)
print(my_numbers[interval2] == my_numbers[:3])  #True