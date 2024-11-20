#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/17


bin_obj = b'Hello'
print(type(bin_obj)) #<class 'bytes'>
print(bin_obj.decode()) #'Hello

#bytes和str是两种数据类型，即便有时看上去"一样"，但做比较时永不相等：
print(b'Hello' == 'Hello') #False