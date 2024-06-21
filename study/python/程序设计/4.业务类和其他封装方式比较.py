#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-06-20

##1.业务类 vs 其他封装方式
'''
业务类对象是负责这个业务的人

（1）业务类 vs 页面对象
页面对象 page object 是出现在selenium官方文档中一种业务封装方式。 这是一种图像界面自动化测试的传统封装方式
页面对象：
    页面 = 元素 + 方法

参照如下伪代码
'''


##页面对象伪代码
class HomePage:
    def xxxElement(self):
        return self.driver.find_element_by_id("some_id")

    def xxxElement2(self):
        return self.driver.find_element_by_id("some_id2")

    def login(self, some_text):
        self.xxxElement.sendkeys(some_text)
        self.xxxElement2.click()
        return ShoppingPage()


class ShoppingPage:
    def xxxElement3(self):
        return self.driver.find_element_by_id("some_id3")

    def xxxElement4(self):
        return self.driver.find_element_by_id("some_id4")

    def buy_someting(self, number):
        self.xxxElement3.sendkeys(number)
        self.xxxElement4.click()
        return ShoppingResultPage()


##调用伪代码
homepage = HomePage()
shopping_page = homepage.login()
shopping_resutl_page = shopping_page.buy_someting(3)
##或者调用链方式
shopping_resutl_page = HomePage().login().buy_someting(4)

'''
问题：
    多个页面出现重复原素
    测试中要重复调用一些常用的业务流程，往往要横跨很多页面

业务类的封装方式
    是普适的，当然适用于图型界面的自动化测试
    在图型界面自动化测试中使用业务类封装


有人认为页面对象在于可以减少页面修改时的代码维护量
    回答：页面多了，同样元素出现不同页面上，仍旧会出现重复元素定义
    另外：如果设计子页面类，然后组合子页面 来避免重复元素定义，则会导致复杂的页面类-----子页面类结构
'''


class Custome:  # 这是一个页面
    def login(self, some_text):
        self.driver.open_url("homepage_url")
        self.driver.find_element_by_id('some_id').sendkeys(some_text)
        self.driver.find_element_by_id("some_id2").click()

    def buy_something(self, number):  # 这是一个页面元素
        self.driver.find_element_by_id("some_id3").sendkeys(number)
        self.driver.find_element_by_id("some_id4").click()


user1 = Custome()
user1.login(some_text='哈哈')
user1.buy_something(number=3)





##2.业务类 VS 关键字驱动
'''
robot framework
    业务封装：python关键字(负责具体实现，工具） 和 robot关键字（表格形式的伪代码---负责业务逻辑）====业务类+工具类
和业务类区别，keyword driven是面向过程的，所谓关键字是一个一个方法，按顺序调用来实现业务逻辑

业务类封装方式：
    面向对象
    业务逻辑= 一个个活生生的人来组成业务逻辑
'''

##3 业务类vs 数据驱动
'''
数据驱动，是重用同一套业务逻辑而使用不同数据的意思。
数据驱动和业务类并没有矛盾，两者可以在一套代码里面共存
'''

