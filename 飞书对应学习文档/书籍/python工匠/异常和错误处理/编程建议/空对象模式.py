#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/25


QUALIFIED_POINTS = 80

class UserPoint:
    """用户得分记录"""

    def __init__(self, username, points):
        self.username = username
        self.points = points

    def is_qualified(self):
        """返回得分是否合格"""
        return self.points >= QUALIFIED_POINTS

class NullUserPoint:
    """一个空的用户得分记录"""

    username = ''
    points = 0

    def is_qualified(self):
        return False

def make_userpoint(point_string):
    """从字符串初始化一条得分记录

    :param point_string: 形如piglei 1 的表示得分记录的字符串
    :return: 如果输入合法，返回 UserPoint 对象，否则返回 NullUserPoint
    """
    try:
        username, points = point_string.split()
        points = int(points)
    except ValueError:
        return NullUserPoint()

    if points < 0:
        return NullUserPoint()
    return UserPoint(username=username, points=points)


def count_qualified(points_data):
    """计算得分合格的总人数

    :param points_data: 字符串格式的用户得分列表
    """
    #这里的make_userpoint()总是会返回一个符合要求的对象（UserPoint()或NullUserPoint()）
    return sum(make_userpoint(s).is_qualified() for s in points_data)


data = [
    'piglei 96',
    'nobody 61',
    'cotton 83',
    'invalid_data',
    'roland $invalid_points',
    'alfred -3',
]

print(count_qualified(data))
# 输出结果：
# 2