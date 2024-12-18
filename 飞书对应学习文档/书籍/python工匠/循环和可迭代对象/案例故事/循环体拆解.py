#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/26
from functools import partial
def read_file_digits(fp, block_size=1024 * 8):
    """生成器函数：分块读取文件内容，返回其中的数字字符"""
    _read = partial(fp.read, block_size)
    for chunk in iter(_read, ''):
        for s in chunk:
            if s.isdigit():
                yield s


#统计函数
def count_digits_v4(fname):
    count = 0
    with open(fname) as file:
        for _ in read_file_digits(file):
            count += 1
    return count


#复用读取函数后，统计偶数函数
from collections import defaultdict
def count_evne_groups(fname):
    count = defaultdict(int)
    with open(fname) as file:
        for digit in read_file_digits(file):
            if int(digit) % 2 == 0:
                count[int(digit)] += 1
    return count


if __name__ == '__main__':
    print(count_digits_v4('small_file.txt')) #13
    print(count_evne_groups('small_file.txt')) #defaultdict(<class 'int'>, {2: 5, 8: 1})