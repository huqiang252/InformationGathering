#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/4
from abc import ABC, abstractmethod
from typing import List

# 观察者接口
class Observer(ABC):
    @abstractmethod
    def update(self, sid: str):
        pass

# 主题接口
class Subject(ABC):
    def __init__(self):
        self._observers: List[Observer] = []

    def attach(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, sid: str):
        for observer in self._observers:
            observer.update(sid)

# 具体主题 - 平台服务
class PlatformService(Subject):
    def __init__(self):
        super().__init__()
        self._sid = None

    @property
    def sid(self):
        return self._sid

    @sid.setter
    def sid(self, value: str):
        self._sid = value
        self.notify(value)

    def login(self, username: str, password: str) -> str:
        # 模拟登录过程
        self._sid = f"sid_{username}_{password}"
        self.notify(self._sid)  # 通知观察者
        return self._sid

    def logout(self):
        self._sid = None
        self.notify(self._sid)  # 通知观察者

# 具体观察者 - 行情服务
class MarketService(Observer):
    def __init__(self, name: str):
        self.name = name
        self.sid = None

    def update(self, sid: str):
        self.sid = sid
        print(f"{self.name} received new SID: {self.sid}")

    def call_http_api(self):
        if self.sid:
            # 模拟调用HTTP接口
            print(f"{self.name} calling HTTP API with SID: {self.sid}")
        else:
            print(f"{self.name} cannot call HTTP API without SID")

# 具体观察者 - 交易服务
class TradeService(Observer):
    def __init__(self, name: str):
        self.name = name
        self.sid = None

    def update(self, sid: str):
        self.sid = sid
        print(f"{self.name} received new SID: {self.sid}")

    def call_http_api(self):
        if self.sid:
            # 模拟调用HTTP接口
            print(f"{self.name} calling HTTP API with SID: {self.sid}")
        else:
            print(f"{self.name} cannot call HTTP API without SID")

# 示例使用
if __name__ == "__main__":
    platform_service = PlatformService()
    market_service = MarketService("MarketService")
    trade_service = TradeService("TradeService")

    platform_service.attach(market_service)
    platform_service.attach(trade_service)

    # 模拟登录
    platform_service.login("user1", "password1")

    # 后续调用HTTP接口
    market_service.call_http_api()
    trade_service.call_http_api()

    # 模拟登出
    platform_service.logout()

    # 再次尝试调用HTTP接口
    market_service.call_http_api()
    trade_service.call_http_api()
