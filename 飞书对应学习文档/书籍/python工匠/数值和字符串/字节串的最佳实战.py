#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/17


def upper_s(input_str):
    '''把输入的字符串中的s都转成大写S'''
    return input_str.replace('s', 'S')


#从外部系统拿到的字节串对象
bin_obj=b'super sunflowers\xef\xbc\x88\xe5\x90\x91\xe6\x97\xa5\xe8\x91\xb5\xef\xbc\x89'


# 将其转换为字符串后，再继续执行后面的操作
str_obj = bin_obj.decode('UTF-8')
print(str_obj) #'super sunflowers（向日葵）'

print( upper_s( str_obj ) ) #'Super SunflowerS.（向日葵）'
