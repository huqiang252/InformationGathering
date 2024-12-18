#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/23

def generate_even(max_number):
    """
    ，其中包含从1到max_number的所有偶数。
    """
    for i in range(0,max_number):
        if i%2==0:
            yield i




#因为生成器是可迭代对象，所以你可以使用list()等函数方便地把它转换为各种其他容器类型
print(list(generate_even(30)))  #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
