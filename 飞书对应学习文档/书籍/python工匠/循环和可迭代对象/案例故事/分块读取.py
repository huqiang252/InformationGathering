#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/26


def count_digits_v2(fname):
    """计算文件里包含多少个数字字符，每次读取 8 KB"""
    count = 0
    block_size = 1024 * 8
    with open(fname) as file:
        while True:
            chunk = file.read(block_size)
            # 当文件没有更多内容时，read 调用将会返回空字符串 ''
            if not chunk:
                break
            for s in chunk:
                if s.isdigit():
                    count += 1
    return count

if __name__ == '__main__':
    print(count_digits_v2('small_file.txt'))