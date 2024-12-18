#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/26
lists = [0, 2, 3, 4, 5,6,7,8,9,10,11,12,13]
print(lists[0:9:2]) #[0, 3, 5, 7, 9]

from itertools import islice
print(islice(lists, 0, 9, 2)) #<itertools.islice object at 0x00000176ECB41400>
print(list(islice(lists, 0, 9, 2))) #[0, 3, 5, 7, 9]
