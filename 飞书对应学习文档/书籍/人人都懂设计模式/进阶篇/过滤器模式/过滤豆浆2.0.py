#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/10
from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法

class Filter(metaclass=ABCMeta):
    """过滤器"""

    @abstractmethod
    def doFilter(self, elements):
        """过滤方法"""
        pass


class FilterChain(Filter):
    """过滤器链"""

    def __init__(self):
        self._filters = []

    def addFilter(self, filter):
        self._filters.append(filter)

    def removeFilter(self, filter):
        self._filters.remove(filter)

    def doFilter(self, elements):
        for filter in self._filters:
            elements = filter.doFilter(elements)
        return elements


class FilterScreen(Filter):
    """过滤网"""

    def doFilter(self, elements):
        for material in elements:
            if (material == "豆渣"):
                elements.remove(material)
        return elements


if __name__ == '__main__':
    rawMaterials = ["豆渣", "豆沙", "豆沙", "豆沙", "豆沙", "豆沙", "豆沙", "豆沙", "豆沙", "豆沙", "豆沙", "豆沙", "豆沙", "豆沙", "豆沙", "豆沙", "豆沙", "豆沙","豆沙", "豆沙", "豆沙", "豆沙",]
    print("过滤前：", rawMaterials)
    filter=FilterScreen()
    filteredMaterials=filter.doFilter(rawMaterials)
    print("过滤后：", filteredMaterials)