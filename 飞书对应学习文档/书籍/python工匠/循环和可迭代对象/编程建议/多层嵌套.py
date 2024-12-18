#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/26


def find_first_word(fp, prefix):
    """找到文件里第一个以指定前缀开头的单词并打印出来

    :param fp: 可读文件对象
    :param prefix: 需要寻找的单词前缀
    """
    for line in fp:
        for word in line.split():
            if word.startswith(prefix):
                return word
    return None

def print_first_word(fp, prefix):
    first_word = find_first_word(fp, prefix)
    if first_word:
        print(f'Found the first word startswith "{prefix}": "{first_word}"')
    else:
        print(f'Word starts with "{prefix}" was not found.')