#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/9
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法

class DataNode(metaclass=ABCMeta):
    """数据结构类"""

    def accept(self, visitor):
        """接受访问者的访问"""
        visitor.visit(self)

class Visitor(metaclass=ABCMeta):
    """访问者"""

    @abstractmethod
    def visit(self, data):
        """对数据对象的访问操作"""
        pass


class ObjectStructure:
    """数据结构的管理类，也是数据对象的一个容器，可遍历容器内的所有元素"""

    def __init__(self):
        self.__datas = []

    def add(self, dataElement):
        self.__datas.append(dataElement)

    def action(self, visitor):
        """进行数据访问的操作"""
        for data in self.__datas:
            data.accept(visitor)


class DesignPatternBook(DataNode):
    """《从生活的角度解读设计模式》一书"""

    def getName(self):
        return "《从生活的角度解读设计模式》"


class Engineer(Visitor):
    """工程师"""

    def visit(self, book):
        print("技术狗读%s一书后的感受：能抓住模式的核心思想，深入浅出，很有见地！" % book.getName())


class ProductManager(Visitor):
    """产品经理"""

    def visit(self, book):
        print("产品经理读%s一书后的感受：配图非常有趣，文章很有层次感！" % book.getName())


class OtherFriend(Visitor):
    """IT圈外的朋友"""

    def visit(self, book):
        print("IT圈外的朋友读%s一书后的感受：技术的内容一脸懵逼，但故事很精彩，像是看小说或是故事集！"
              % book.getName())


if __name__ == '__main__':
    book = DesignPatternBook()
    objMgr = ObjectStructure()
    objMgr.add(book)
    fans = [Engineer(),ProductManager(),OtherFriend()]
    for fan in fans:
        objMgr.action(fan)