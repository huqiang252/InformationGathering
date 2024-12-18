#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/26

numbers = [1,2,3]
numbers = (i*2 for i in numbers)

print(4 in numbers) #True
print(4 in numbers) #False  这种由生成器的“耗尽”特性所导致的bug，隐蔽性非常强，当它出现在一些复杂项目中时，尤其难定位