#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/26


#普通解法
def parse_titles(filename):
    """从隔行数据文件中读取 Reddit 主题名称
    """
    with open(filename, 'r') as fp:
        for i, line in enumerate(fp):
            # 跳过无意义的--- 分隔符
            if i % 2 == 0:
                yield line.strip()


##使用islice
from itertools import islice
def parse_titles_v2(filename):
    with open(filename, 'r') as fp:
        # 设置 step=2，跳过无意义的--- 分隔符
        for line in islice(fp, 0, None, 2):
            yield line.strip()