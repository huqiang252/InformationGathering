#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/5
from abc import ABCMeta,abstractmethod

from enum import Enum
import uuid
class DeviceType(Enum):
    '''设备类型'''
    TypeSpeaker = 1
    TypeMicrophone = 2
    TypeCamera = 3


class DeviceItem:
    '''设备项'''
    def __init__(self,id,name,type,isDefault=False):
        self.__id = id
        self.__name = name
        self.__type = type
        self.__isDefault = isDefault


    def __str__(self):
        return f'type:{self.__type},id:{self.__id},name:{self.__name},isDefault:{self.__isDefault}'

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getType(self):
        return self.__type

    def isDefault(self):
        return self.__isDefault


class DeviceList:
    '''设备列表'''
    def __init__(self):
        self.__devices = []

    def add(self,item):
        self.__devices.append(item)

    def getCount(self):
        return len(self.__devices)

    def getByIdx(self,idx)->DeviceItem:
        if idx<0 or idx>=self.getCount():
            return None
        return self.__devices[idx]

    def getById(self,id)->DeviceItem:
        for item in self.__devices:
            if item.getId() == id:
                return item

class DeviceMgr(metaclass=ABCMeta):
    '''设备管理器'''
    @abstractmethod
    def enumerate(self):
        '''枚举设备列表（程序初始化，有设备插拔时都需要重新获取设备列表）'''
        pass
    @abstractmethod
    def active(self,deviceId):
        '''激活设备'''
        pass

    @abstractmethod
    def getCurDeviceId(self):
        '''获取当前激活的设备ID'''
        pass


class SpeakerMgr(DeviceMgr):
    '''扬声器管理器'''

    def __init__(self):
        self.__curDeviceId = None

    def enumerate(self):
        '''枚举设备列表'''
        devices = DeviceList()
        devices.add(DeviceItem(uuid.uuid4(),'扬声器1',DeviceType.TypeSpeaker))
        devices.add(DeviceItem(uuid.uuid4(),'扬声器2',DeviceType.TypeSpeaker,True))
        return devices

    def active(self,deviceId):
        '''激活设备'''
        self.__curDeviceId = deviceId

    def getCurDeviceId(self):
        '''获取当前激活的设备ID'''
        return self.__curDeviceId


class MicrophoneMgr(DeviceMgr):
    '''麦克风管理器'''
    def __init__(self):
        self.__curDeviceId = None

    def enumerate(self):
        '''枚举设备列表'''
        devices = DeviceList()
        devices.add(DeviceItem(uuid.uuid4(),'麦克风1',DeviceType.TypeMicrophone))
        devices.add(DeviceItem(uuid.uuid4(),'麦克风2',DeviceType.TypeMicrophone,True))
        return devices
    def active(self,deviceId):
        '''激活设备'''
        self.__curDeviceId = deviceId

    def getCurDeviceId(self):
        '''获取当前激活的设备ID'''
        return self.__curDeviceId



class DeviceUtil:
    '''设备工具类'''

    def __init__(self):
        self.__mgrs = {}
        self.__mgrs[DeviceType.TypeSpeaker] = SpeakerMgr()
        self.__mgrs[DeviceType.TypeMicrophone] = MicrophoneMgr()


    def __getDeviceMgr(self,type):
        return self.__mgrs[type]

    def getDeviceList(self,type):
        return self.__getDeviceMgr(type).enumerate()

    def active(self,type,deviceId):
        self.__getDeviceMgr(type).active(deviceId)

    def getCurDeviceId(self,type):
        return self.__getDeviceMgr(type).getCurDeviceId()




if __name__ == '__main__':
    deviceUtil = DeviceUtil()
    deviceList = deviceUtil.getDeviceList(DeviceType.TypeSpeaker)
    print('麦克风设备列表：')
    if deviceList.getCount() > 0:
        deviceUtil.active(DeviceType.TypeSpeaker,deviceList.getByIdx(0).getId()) #设置第一个设备激活

    for idx in range(deviceList.getCount()):
        device = deviceList.getByIdx(idx)
        print(device)

    print(f'当前使用的设备：{deviceList.getById(deviceUtil.getCurDeviceId(DeviceType.TypeSpeaker)).getName()}')