#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发团队：行情组
# 开发人员： huqiang
# datetime： 2024/11/30
# 文件名称   ：圈复杂都.PY

def rank(self):
    rating_num = float(self.rating)
    if rating_num >= 8.5:
        return 'S'
    elif rating_num >= 8:
        return 'A'
    elif rating_num >= 7:
        return 'B'
    elif rating_num >= 6:
        return 'C'
    else:
        return 'D'