#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/22


from collections.abc import MutableMapping
from collections import defaultdict
from enum import Enum

class PagePerfLevel(str, Enum):
    LT_100 = 'Less than 100 ms'
    LT_300 = 'Between 100 and 300 ms'
    LT_1000 = 'Between 300 ms and 1 s'
    GT_1000 = 'Greater than 1 s'

class PerfLevelDict(MutableMapping):
    """存储响应时间性能等级的字典"""
    def __init__(self):
        self.data = defaultdict(int)
    def __getitem__(self, key):
        """当某个级别不存在时，默认返回 0"""
        return self.data[self.compute_level(key)]
    def __setitem__(self, key, value):
        """将 key 转换为对应的性能等级，然后设置值"""
        self.data[self.compute_level(key)] = value
    def __delitem__(self, key):
        del self.data[key]
    def __iter__(self):
        return iter(self.data)
    def __len__(self):
        return len(self.data)
    @staticmethod
    def compute_level(time_cost_str):
        """根据响应时间计算性能等级"""
        # 假如已经是性能等级，不做转换直接返回
        if time_cost_str in list(PagePerfLevel):
            return time_cost_str
        time_cost = int(time_cost_str)
        if time_cost < 100:
            return PagePerfLevel.LT_100
        elif time_cost < 300:
            return PagePerfLevel.LT_300
        elif time_cost < 1000:
            return PagePerfLevel.LT_1000
        return PagePerfLevel.GT_1000




if __name__ == '__main__':
    d = PerfLevelDict()
    d[50] +=1
    d[403] +=12
    d[30]+=2
    print(dict(d))  #{<PagePerfLevel.LT_100: 'Less than 100 ms'>: 3, <PagePerfLevel.LT_1000: 'Between 300 ms and 1 s'>: 12}