#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/10

from abc import ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法

class Template(metaclass=ABCMeta):
    """模板类(抽象类)"""

    @abstractmethod
    def stepOne(self):
        pass

    @abstractmethod
    def stepTwo(self):
        pass

    @abstractmethod
    def stepThree(self):
        pass

    def templateMethold(self):
        """模板方法"""
        self.stepOne()
        self.stepTwo()
        self.stepThree()


class TemplateImplA(Template):
    """模板实现类A"""

    def stepOne(self):
        print("步骤一")

    def stepTwo(self):
        print("步骤二")

    def stepThree(self):
        print("步骤三")


class TemplateImplB(Template):
    """模板实现类B"""

    def stepOne(self):
        print("Step one")

    def stepTwo(self):
        print("Step two")

    def stepThree(self):
        print("Step three")
