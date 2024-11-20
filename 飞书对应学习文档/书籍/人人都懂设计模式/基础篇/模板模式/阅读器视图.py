#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/10


from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法

class ReaderView(metaclass=ABCMeta):
    """阅读器视图"""

    def __init__(self):
        self.__curPageNum = 1

    def getPage(self, pageNum):
        self.__curPageNum = pageNum
        return "第" + str(pageNum) + "的内容"

    def prePage(self):
        """模板方法，往前翻一页"""
        content = self.getPage(self.__curPageNum - 1)
        self._displayPage(content)

    def nextPage(self):
        """模板方法，往后翻一页"""
        content = self.getPage(self.__curPageNum + 1)
        self._displayPage(content)

    @abstractmethod
    def _displayPage(self, content):
        """翻页效果"""
        pass


class SmoothView(ReaderView):
    """左右平滑的视图"""

    def _displayPage(self, content):
        print("左右平滑:" + content)


class SimulationView(ReaderView):
    """仿真翻页的视图"""

    def _displayPage(self, content):
        print("仿真翻页:" + content)


if __name__ == '__main__':
    smoothView = SmoothView()
    smoothView.nextPage()
    smoothView.prePage()

    print()

    simulationView=SimulationView()
    simulationView.nextPage()
    simulationView.prePage()
    simulationView.nextPage()
