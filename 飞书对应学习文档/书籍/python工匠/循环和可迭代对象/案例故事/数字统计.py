#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/26


def count_digits(fname):
    """计算文件里包含多少个数字字符"""
    count = 0
    with open(fname) as file:
        for line in file:
            for s in line:
                if s.isdigit():
                    count += 1
    return count


if __name__ == '__main__':
    print(count_digits('small_file.txt')) #13