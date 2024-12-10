#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发团队：行情组
# 开发人员： huqiang
# datetime： 2024/11/30
# 文件名称   ：圈复杂2.PY


from bisect import bisect


def rank(self):
    breakpoints = (6,7,8,8.5)
    grades = ('D','C','B','A','S')
    index = bisect(breakpoints, self.rating)
    return grades[index]



