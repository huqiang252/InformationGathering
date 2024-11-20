#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/7

from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法

class SocketEntity:
    """接口类型定义"""

    def __init__(self, numOfPin, typeOfPin):
        self.__numOfPin = numOfPin
        self.__typeOfPin = typeOfPin

    def getNumOfPin(self):
        return self.__numOfPin

    def setNumOfPin(self, numOfPin):
        self.__numOfPin = numOfPin

    def getTypeOfPin(self):
        return self.__typeOfPin

    def setTypeOfPin(self, typeOfPin):
        self.__typeOfPin = typeOfPin


class ISocket(metaclass=ABCMeta):
    """插座类型"""

    def getName(self):
        """插座名称"""
        pass

    def getSocket(self):
        """获取接口"""
        pass


class ChineseSocket(ISocket):
    """国标插座"""

    def getName(self):
        return  "国标插座"

    def getSocket(self):
        return SocketEntity(3, "八字扁型")


class BritishSocket:
    """英标插座"""

    def name(self):
        return  "英标插座"

    def socketInterface(self):
        return SocketEntity(3, "T字方型")

class AdapterSocket(ISocket):
    """插座转换器"""

    def __init__(self, britishSocket):
        self.__britishSocket = britishSocket

    def getName(self):
        return  self.__britishSocket.name() + "转换器"

    def getSocket(self):
        socket = self.__britishSocket.socketInterface()
        socket.setTypeOfPin("八字扁型")
        return socket


def canChargeforDigtalDevice(name, socket):
    if socket.getNumOfPin() == 3 and socket.getTypeOfPin() == "八字扁型":
        isStandard = "符合"
        canCharge = "可以"
    else:
        isStandard = "不符合"
        canCharge = "不能"


    print( f"[{name}]：\n针脚数量：{socket.getNumOfPin()}，针脚类型：{socket.getTypeOfPin()}； {isStandard}中国标准，{canCharge}给大陆的电子设备充电！")


if __name__ == '__main__':
    chineseSocket = ChineseSocket()
    canChargeforDigtalDevice(chineseSocket.getName(), chineseSocket.getSocket())

    britishSocket = BritishSocket()
    canChargeforDigtalDevice(britishSocket.name(),britishSocket.socketInterface())


    adapterSocket = AdapterSocket(britishSocket)
    canChargeforDigtalDevice(adapterSocket.getName(), adapterSocket.getSocket())
