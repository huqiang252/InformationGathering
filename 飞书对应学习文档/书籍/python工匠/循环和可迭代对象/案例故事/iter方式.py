#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/26

from functools import partial
def count_digits_v3(fname):
    count = 0
    block_size = 1024 * 8
    with open(fname) as fp:
        # 使用functools.partial 构造一个新的无须参数的函数
        _read = partial(fp.read, block_size)
        # 利用iter() 构造一个不断调用_read 的迭代器
        for chunk in iter(_read, ''):
            for s in chunk:
                if s.isdigit():
                    count += 1
    return count

if __name__ == '__main__':
    print(count_digits_v3('small_file.txt'))