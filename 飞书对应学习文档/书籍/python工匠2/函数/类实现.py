#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发团队：行情组
# 开发人员： huqiang
# datetime： 2024/11/30
# 文件名称   ：类实现.PY

import re

class CyclicMosaic:
    """使用会轮换的屏蔽字符，基于类实现"""
    _chars = ['*', 'x']
    def __init__(self):
        self._char_index = 0  #类实例状态一般在初始化时设置，而不是在函数内部设置
    def generate(self, matchobj):
        char = self._chars[self._char_index]
        self._char_index = (self._char_index + 1) % len(self._chars)
        length = len(matchobj.group())
        return char * length


def mosaic_string(string):
    '''用*替换输入字符里面所有的连续数字'''

    #此处是make_cyclic_mosaic()而不是make_cyclic_mosaic，因为make_cyclic_mosaic()函数的调用结果才是真正的替换函数
    return re.sub(r'\d+', CyclicMosaic().generate, string)  #


if __name__ == '__main__':
    print(mosaic_string('商店共100个苹果，小明以12元每斤的价格买走了8个'))  #商店共***个苹果，小明以xx元每斤的价格买走了*个
    print(mosaic_string('商店共100个苹果，小明以12元每斤的价格买走了8个'))  #商店共***个苹果，小明以xx元每斤的价格买走了*个
    print(mosaic_string('商店共100个苹果，小明以12元每斤的价格买走了8个'))  #商店共***个苹果，小明以xx元每斤的价格买走了*个


