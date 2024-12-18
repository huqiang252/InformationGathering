#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/26


def query_users(limit, offset, min_followers_count, include_profile):
    """查询用户
    :param min_followers_count: 最小关注者数量
    :param include_profile: 结果包含用户详细档案
    """
    ...


#位置参数调用：时间长了，谁能知道 100和True 分别代表什么呢？
query_users(20, 0, 100, True)



query_users(limit=20, offset=0, min_followers_count=100, include_profile=True)
# 关键字参数可以不严格按照函数定义参数的顺序来传递
query_users(min_followers_count=100, include_profile=True, limit=20, offset=0)