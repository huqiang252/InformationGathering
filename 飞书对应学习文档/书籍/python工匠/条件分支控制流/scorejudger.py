#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/24


class ScoreJudger:
    '''仅当分数大于60为真'''
    def __init__(self,score):
        self.score = score


    def __bool__(self):
        return self.score > 60


if __name__ == '__main__':
    sj = ScoreJudger(60)
    print(bool(sj)) #False
    if sj:
        print('我60分')

    sj2 = ScoreJudger(70)
    print(bool(sj2)) #True

    if sj2:
        print('我70分') #我70分
