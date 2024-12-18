#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/24

from collections import OrderedDict

nums = [10,2,3,21,10,3]
print(set(nums))  #{3,10,2,21}

#调用fromkeys方法会创建一个有序字典对象。字典的键来自方法的第一个参数：可迭代对象（此处为nums列表），字典的值默认为None
res = OrderedDict.fromkeys(nums).keys()
print(res) #odict_keys([10, 2, 3, 21])


print(list(res))  #[10, 2, 3, 21]