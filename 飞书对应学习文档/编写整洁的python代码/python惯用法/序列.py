#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2025/1/12
# 文件名称   ：序列.py


from collections.abc import Sequence

class Items(Sequence):
    def __init__(self, *values):
        self._values = list(values)

    def __len__(self):
        return len(self._values)

    def __getitem__(self, item):
        return self._values.__getitem__(item)



if __name__ == '__main__':
    items = Items(1, 2, 3)
    print(items[0])
    print(items[1:])  # 切片[2, 3]