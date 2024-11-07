#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/6


from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法

class ReceiveParcel(metaclass=ABCMeta):
    """接收包裹抽象类"""

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    @abstractmethod
    def receive(self, parcelContent):
        pass


class TonyReception(ReceiveParcel):
    """Tony接收"""

    def __init__(self, name, phoneNum):
        super().__init__(name)
        self.__phoneNum = phoneNum

    def getPhoneNum(self):
        return self.__phoneNum

    def receive(self, parcelContent):
        print("货物主人：%s，手机号：%s" % (self.getName(), self.getPhoneNum()) )
        print("接收到一个包裹，包裹内容：%s" % parcelContent)


class WendyReception(ReceiveParcel):
    """Wendy代收"""

    def __init__(self, name, receiver):
        super().__init__(name)
        self.__receiver = receiver

    def receive(self, parcelContent):
        print("我是%s的朋友，我来帮他代收快递！" % (self.__receiver.getName() + "") )
        if(self.__receiver is not None):
            self.__receiver.receive(parcelContent)
        print("代收人：%s" % self.getName())


if __name__ == '__main__':
    tony = TonyReception("Tony", "123456789")
    print('tony接受')
    tony.receive("爆米花")
    print()

    print('wendy代收')
    wendy = WendyReception("Wendy", tony)
    wendy.receive('爆米花')