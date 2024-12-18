#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/11/30
# 文件名称   ：countVowels.py



def count_vowels(fp):
    """统计某个文件中元音字母（aeiou）的数量"""
    if not hasattr(fp, 'read'):
        raise TypeError('must provide a valid file object')

    VOWELS_LETTERS = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for line in fp:
        for char in line:
            if char.lower() in VOWELS_LETTERS:
                count += 1
    return count


class StringList:
    def __init__(self,strings):
        self.strings = strings

    def read(self):
        return ''.join(self.strings)

    def __iter__(self):
        for s in self.strings:
            yield s



if __name__ == '__main__':
    print(count_vowels(StringList(['hello', 'world']))) #3
