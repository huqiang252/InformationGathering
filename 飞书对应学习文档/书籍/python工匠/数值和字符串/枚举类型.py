#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/18

#用户每日奖励积分数量
DAILY_POINTS_REWARDS = 100
# VIP 用户每日额外奖励积分数量
VIP_EXTRA_POINTS = 20

from enum import Enum
# 在定义枚举类型时，如果同时继承一些基础类型，比如int、str，
# 枚举类型就能同时充当该基础类型使用。比如在这里，UserType 就可以当作int 使用
class UserType(int, Enum):
    # VIP 用户
    VIP = 3
    # 小黑屋用户
    BANNED = 13


def add_daily_points(user):
    """用户每天完成第一次登录后，为其增加积分"""
    if user.type == UserType.BANNED:
        return
    if user.type == UserType.VIP:
        user.points += DAILY_POINTS_REWARDS + VIP_EXTRA_POINTS
        return
    user.points += DAILY_POINTS_REWARDS
    return

