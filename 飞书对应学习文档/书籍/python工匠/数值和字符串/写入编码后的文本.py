#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/17
def upper_s(input_str):
    '''把输入的字符串中的s都转成大写S'''
    return input_str.replace('s', 'S')

#通过 encoding指定字符串编码格式为 UTF-8
with open('output.txt', 'w', encoding='UTF-8') as fp:
    str_obj = upper_s('super sunflowers（向日葵）')
    fp.write(str_obj)
    # 最后 output.txt 中存储的将是UTF-8 编码的文本