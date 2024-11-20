#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/9
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法

class DesignPatternBook:
    """《从生活的角度解读设计模式》一书"""
    def getName(self):
        return "《从生活的角度解读设计模式》"


class Reader(metaclass=ABCMeta):
    """访问者，也就是读者"""

    @abstractmethod
    def read(self, book):
        pass

class Engineer(Reader):
    """工程师"""

    def read(self, book):
        print("技术狗读%s一书后的感受：能抓住模式的核心思想，深入浅出，很有见地！" % book.getName())


class ProductManager(Reader):
    """产品经理"""

    def read(self, book):
        print("产品经理读%s一书后的感受：配图非常有趣，文章很有层次感！" % book.getName())

class OtherFriend(Reader):
    """IT圈外的朋友"""

    def read(self, book):
        print("IT圈外的朋友读%s一书后的感受：技术的内容一脸懵逼，但故事很精彩，像是看小说或是故事集！"
              % book.getName())


if __name__ == '__main__':
    book = DesignPatternBook()
    fans = [Engineer(),ProductManager(),OtherFriend()]
    for fan in fans:
        fan.read(book)