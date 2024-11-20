#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/10


class PowerBank:
    """移动电源"""

    def __init__(self, serialNum, electricQuantity):
        self.__serialNum = serialNum
        self.__electricQuantity = electricQuantity
        self.__user = ""

    def getSerialNum(self):
        return self.__serialNum

    def getElectricQuantity(self):
        return self.__electricQuantity

    def setUser(self, user):
        self.__user = user

    def getUser(self):
        return self.__user

    def showInfo(self):
        print("序列号:%s 电量:%d%%  使用者:%s" % (self.__serialNum, self.__electricQuantity, self.__user) )


class ObjectPack:
    """对象的包装类
    封装指定的对象(如充电宝)是否被使用中"""
    def __init__(self, obj, inUsing = False):
        self.__obj = obj
        self.__inUsing = inUsing

    def inUsing(self):
        return self.__inUsing

    def setUsing(self, isUsing):
        self.__inUsing = isUsing

    def getObj(self):
        return self.__obj


class PowerBankBox:
    """存放移动电源的智能箱盒"""

    def __init__(self):
        self.__pools = {}
        self.__pools["0001"] = ObjectPack(PowerBank("0001", 100))
        self.__pools["0002"] = ObjectPack(PowerBank("0002", 100))

    def borrow(self, serialNum):
        """借用移动电源"""
        item = self.__pools.get(serialNum)
        result = None
        if(item is None):
            print("没有可用的电源！")
        elif(not item.inUsing()):
            item.setUsing(True)
            result = item.getObj()
        else:
            print("%s电源 已被借用！" % serialNum)
        return result

    def giveBack(self, serialNum):
        """归还移动电源"""
        item = self.__pools.get(serialNum)
        if(item is not None):
            item.setUsing(False)
            print("%s电源 已归还!" % serialNum)

if __name__ == '__main__':
    box = PowerBankBox()
    powerBank1 = box.borrow( "0001" )
    if (powerBank1 is not None):
        powerBank1.setUser( "Tony" )
        powerBank1.showInfo()
    powerBank2 = box.borrow( "0002" )
    if (powerBank2 is not None):
        powerBank2.setUser( "Sam" )
        powerBank2.showInfo()
    powerBank3 = box.borrow( "0001" )
    box.giveBack( "0001" )
    powerBank3 = box.borrow( "0001" )
    if (powerBank3 is not None):
        powerBank3.setUser( "Aimee" )
        powerBank3.showInfo()