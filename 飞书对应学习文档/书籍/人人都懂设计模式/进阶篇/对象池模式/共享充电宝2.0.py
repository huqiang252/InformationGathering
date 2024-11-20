#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/10
from abc import ABCMeta,abstractmethod
import logging
import time

logging.basicConfig(level=logging.INFO)
# 如果想在控制台打印INFO以上的信息，则加上此配制

class PooledObject:
    """池对象,也称池化对象"""

    def __init__(self, obj):
        self.__obj = obj
        self.__busy = False

    def getObject(self):
        return self.__obj

    def setObject(self, obj):
        self.__obj = obj

    def isBusy(self):
        return self.__busy

    def setBusy(self, busy):
        self.__busy = busy

    def __str__(self):
        return f'{id(self.__obj)}, 是否被占用：{self.__busy}'

class ObjectPool(metaclass=ABCMeta):
    """对象池"""

    """对象池初始化大小"""
    InitialNumOfObjects = 10
    """对象池最大的大小"""
    MaxNumOfObjects = 50

    def __init__(self):
        self.__pools = []
        for i in range(0, ObjectPool.InitialNumOfObjects):
            obj = self.createPooledObject()
            print(f"初始化对象池，添加对象{obj}")
            self.__pools.append(obj)
        print(f"初始化对象池大小为{len(self.__pools)}"  )


    @abstractmethod
    def createPooledObject(self):
        """创建池对象, 由子类实现该方法"""
        pass

    def borrowObject(self):
        """借用对象"""
        # 如果找到空闲对象，直接返回
        obj = self._findFreeObject()
        if(obj is not None):
            logging.info("%x对象已被借用, time:%s", id(obj),
                         time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())) )
            print(f'空闲对象池中，对象{id(obj)}被返回')
            return obj
        # 如果对象池未满，则添加新的对象
        if(len(self.__pools) < ObjectPool.MaxNumOfObjects):
            pooledObj = self.addObject()
            if (pooledObj is not None):
                pooledObj.setBusy(True)
                logging.info("%x对象已被借用, time:%s", id(obj),
                             time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
                return pooledObj.getObject()
        # 对象池已满且没有空闲对象，则返回None
        return None

    def returnObject(self, obj):
        """归还对象"""
        for pooledObj in self.__pools:
            if(pooledObj.getObject() == obj):
                pooledObj.setBusy(False)
                logging.info("%x对象已归还, time:%s", id(obj),
                             time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
                break

    def addObject(self):
        """添加新对象"""
        obj = None
        if(len(self.__pools) < ObjectPool.MaxNumOfObjects):
            obj = self.createPooledObject()
            self.__pools.append(obj)
            logging.info("添加新对象%x, time:", id(obj),
                         time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
        return obj

    def clear(self):
        """清空对象池"""
        self.__pools.clear()

    def _findFreeObject(self):
        """查找空闲的对象"""
        obj = None
        for pooledObj in self.__pools:
            if(not pooledObj.isBusy()):
                obj = pooledObj.getObject()
                pooledObj.setBusy(True)
                break
        return obj


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
        print("序列号:%03d  电量:%d%%  使用者:%s" % (self.__serialNum, self.__electricQuantity, self.__user))

class PowerBankPool(ObjectPool):
    """存放移动电源的智能箱盒"""

    __serialNum = 0

    @classmethod
    def getSerialNum(cls):
        cls.__serialNum += 1
        return cls.__serialNum


    def createPooledObject(self):
        powerBank = PowerBank(PowerBankPool.getSerialNum(), 100)
        return PooledObject(powerBank)


if __name__ == '__main__':
    powerBankPool = PowerBankPool()
    powerBank1 = powerBankPool.borrowObject()
    if (powerBank1 is not None):
        powerBank1.setUser( "Tony" )
        powerBank1.showInfo()
    powerBank2 = powerBankPool.borrowObject()
    if (powerBank2 is not None):
        powerBank2.setUser( "Sam" )
        powerBank2.showInfo()
    powerBankPool.returnObject( powerBank1 )
    # powerBank1归还后，不能再对其进行相关操作
    powerBank3 = powerBankPool.borrowObject()
    if (powerBank3 is not None):
        powerBank3.setUser( "Aimee" )
        powerBank3.showInfo()

    powerBankPool.returnObject( powerBank2 )
    powerBankPool.returnObject( powerBank3 )
    powerBankPool.clear()