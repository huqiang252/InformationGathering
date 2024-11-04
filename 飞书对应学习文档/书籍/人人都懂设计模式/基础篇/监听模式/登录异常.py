#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/3
from abc import ABCMeta,abstractmethod
import time
class Observer(metaclass=ABCMeta):
    """观察者的基类"""

    @abstractmethod
    def update(self, observable, object):
        pass


class Observable:
    """被观察者的基类"""

    def __init__(self):
        self.__observers = []

    def addObserver(self, observer):
        self.__observers.append(observer)

    def removeObserver(self, observer):
        self.__observers.remove(observer)

    def notifyObservers(self, object=0):
        for o in self.__observers:
            o.update(self, object)




class Account(Observable):
    def __init__(self):
        super().__init__()
        self.__latestIp = {}
        self.__latestRegion = {}


    def login(self,name,ip,time):
        region = self.__getRegion(ip)
        if self.__isLongDistance(name,region):
            self.notifyObservers({"name":name,"ip":ip,"time":time,"region":region})
        self.__latestRegion[name] = region
        self.__latestIp[name]=ip


    def __getRegion(self,ip):
        ipRegions = {
            '101.47.18.9':'浙江省杭州市',
            '67.218.147.69':'美国洛杉矶'
        }
        region = ipRegions.get(ip)
        return "" if region is None else region


    def __isLongDistance(self,name,region):
        latestRegion = self.__latestRegion.get(name)
        return latestRegion is not None and latestRegion != region

    def __str__(self):
        return f"最近的ip:{self.__latestIp}, 最近一次的区域:{self.__latestRegion}"


class SmsSender(Observer):

    def update(self,observable,object):
        print(f"【短信发送】{object['name']}你好！检测你的账号可能登录异常。最近一次的登录信息：\n \
        登录地区：{object['region']},登录Ip：{object['ip']},登录时间：{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(object['time']))}")


class MailSender(Observer):
    def update(self,observable,object):
        print(f"【邮件发送】{object['name']}你好！检测你的账号可能登录异常。最近一次的登录信息：\n \
        登录地区：{object['region']},登录Ip：{object['ip']},登录时间：{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(object['time']))}")




if __name__ == '__main__':
    accout = Account()
    accout.addObserver(SmsSender())
    accout.addObserver(MailSender())
    accout.login("Tony","101.47.18.9",time.time())
    print(accout)
    accout.login("Tony","67.218.147.69",time.time())
    print(accout)