#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-07-24

'''
一个正整数的阶乘 factorial 是所有小于及等于该数的正整数的积，并且 0 的阶乘为 1。自然数 n 的阶乘写作 n!。

对阶乘的定义进行分析：

首先定义 f(n) 为阶乘函数。它的结果就是阶乘计算之后的值。
从定义中能得到基本情况为: f(0) = 1, f(1) = 1
其它情况: f(2) = 2*1 = 2*f(1)，f(3) = 3*2*1 = 3*f(2) 即 f(n) = f(n-1) * n

'''

def f(n):
    """
    实现计算 n 的阶乘
    return：n 阶乘计算之后的值
    """
    if n == 0 or n == 1:
        # 对应基本情况
        return 1
    return f(n - 1) * n  # 对应递归情况



if __name__ == '__main__':
    print(f(5))