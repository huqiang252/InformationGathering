#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/20


results = (n*100 for n in range(10) if n%2==0)
print(results)  #生成器对象 <generator object <genexpr> at 0x000001C6CC088890>

print(tuple(results)) #(0, 200, 400, 600, 800)