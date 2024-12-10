#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/2
# 文件名称   ：hashbyValue.py



class HashByValue:
    """根据 value 属性计算哈希值"""

    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return hash(self.value)



if __name__ == '__main__':
    h = HashByValue('3')
    s = set()
    s.add(h)
    print(h in s) #True
    h.value=4
    print(h in s) #False