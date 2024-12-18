#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/20


d1 = {'foo':3,'bar':4}
res = {key:value*10 for key,value in d1.items() if key == 'foo'}
print(res) #{'foo': 30}