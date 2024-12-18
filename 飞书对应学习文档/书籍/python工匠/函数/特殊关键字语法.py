#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/26


#注意参数列表中的* 符号
def query_users(limit, offset, *, min_followers_count, include_profile):
    """查询用户
    :param min_followers_count: 最小关注者数量
    :param include_profile: 结果包含用户详细档案
    """
    ...

#错误调用方式
query_users(20, 0, 100, True)  #执行报错
# TypeError: query_users() takes 2 positional arguments but 4 were given

#正确调用方式
query_users(20, 0, min_followers_count=100, include_profile=True)