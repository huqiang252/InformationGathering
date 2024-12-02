#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/1
# 文件名称   ：threeFactory.py


class ThreeFactory:
    """在被迭代时不断返回 3
    :param repeat: 重复次数
    """
    def __init__(self, repeat):
        self.repeat = repeat
    def __iter__(self):
        for _ in range(self.repeat):
            yield 3







if __name__ == '__main__':
    from collections.abc import  Iterable
    print(isinstance(ThreeFactory(2),Iterable))  #True