#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/10
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法

class Skill(metaclass=ABCMeta):
    """技能的抽象类"""

    @abstractmethod
    def performance(self):
        """技能表演"""
        pass

class NewEmployee:
    """公司新员工"""

    def __init__(self, name):
        self.__name = name

    def doPerformance(self, skill):
        print(self.__name + "的表演:", end="")
        skill.performance()

class Sing(Skill):
    """唱歌"""
    def performance(self):
        print("唱一首歌")

class Joke(Skill):
    """说段子"""
    def performance(self):
        print("说一搞笑段子")

class Dling(Skill):
    """拉Ukulele"""
    def performance(self):
        print("拉一曲Ukulele")

class PerformMagicTricks(Skill):
    """表演魔术"""
    def performance(self):
        print("神秘魔术")

class Skateboarding(Skill):
    """玩滑板"""
    def performance(self):
        print("酷炫滑板")

if __name__ == '__main__':
    helen = NewEmployee( "Helen" )
    helen.doPerformance( Sing() )
    frank = NewEmployee( "Frank" )
    frank.doPerformance( Dling() )
    jacky = NewEmployee( "Jacky" )
    jacky.doPerformance( Joke() )
    chork = NewEmployee( "Chork" )
    chork.doPerformance( PerformMagicTricks() )
    Kerry = NewEmployee( "Kerry" )
    Kerry.doPerformance( Skateboarding() )

