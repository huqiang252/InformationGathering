#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/9


import logging
# 引入logging模块记录异常

class Pigment:
    """颜料"""

    def __init__(self, color):
        self.__color = color
        self.__user = ""

    def getColor(self):
        return self.__color

    def setUser(self, user):
        self.__user = user
        return self

    def showInfo(self):
        print("%s 取得 %s色颜料"  % (self.__user, self.__color) )

class PigmengFactory:
    """资料的工厂类"""

    def __init__(self):
        self.__sigmentSet = {
            "红": Pigment("红"),
            "黄": Pigment("黄"),
            "蓝": Pigment("蓝"),
            "绿": Pigment("绿"),
            "紫": Pigment("紫"),
        }

    def getPigment(self, color):
        pigment = self.__sigmentSet.get(color)
        if pigment is None:
            logging.error("没有%s颜色的颜料！", color)
        return pigment


if __name__ == '__main__':
    factory = PigmengFactory()
    pigmentRed = factory.getPigment( "红" ).setUser( "梦之队" )
    pigmentRed.showInfo()
    pigmentRed2 = factory.getPigment( "红" ).setUser( "和平队" )
    pigmentRed2.showInfo()
    pigmentYellow = factory.getPigment( "黄" ).setUser( "梦之队" )
    pigmentYellow.showInfo()
    pigmentBlue1 = factory.getPigment( "蓝" ).setUser( "梦之队" )
    pigmentBlue1.showInfo()
    pigmentBlue2 = factory.getPigment( "蓝" ).setUser( "和平队" )
    pigmentBlue2.showInfo()
