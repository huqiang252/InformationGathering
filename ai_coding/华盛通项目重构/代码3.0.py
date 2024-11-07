#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/5


import logging
from abc import ABC, abstractmethod
from typing import List
import threading
from http_untils import HttpUtils, MarketCode, Lang

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 观察者接口
class Observer(ABC):
    @abstractmethod
    def update(self, sid: str):
        pass

# 主题接口
class Subject(ABC):
    def __init__(self):
        self._observers: List[Observer] = []
        self._lock = threading.Lock()

    def attach(self, observer: Observer):
        with self._lock:
            if observer not in self._observers:
                self._observers.append(observer)
                logging.info(f"Attached observer: {observer}")

    def detach(self, observer: Observer):
        with self._lock:
            try:
                self._observers.remove(observer)
                logging.info(f"Detached observer: {observer}")
            except ValueError:
                logging.warning(f"Observer not found: {observer}")

    def notify(self, sid: str):
        with self._lock:
            for observer in self._observers:
                observer.update(sid)
                logging.info(f"Notified observer: {observer}")

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
        try:
            self._sid = f"sid_{username}_{password}"
            self.notify(self._sid)  # 通知观察者
            logging.info(f"User {username} logged in successfully")
            return self._sid
        except Exception as e:
            logging.error(f"Login failed: {e}")
            return None

    def logout(self):
        try:
            self._sid = None
            self.notify(self._sid)  # 通知观察者
            logging.info(f"User logged out successfully")
        except Exception as e:
            logging.error(f"Logout failed: {e}")

    def call_http_api(self, market_code: str, env: str, buzz: dict):
        ApiCaller.call_http_api(market_code, env, buzz, self._sid)
        logging.info(f"Called HTTP API for market code: {market_code}, env: {env}, buzz: {buzz}")

# 工具类 - API 调用
class ApiCaller:
    @staticmethod
    def call_http_api(market_code: str, env: str, buzz: dict, sid: str):
        HttpUtils.call_http_api(market_code, env, buzz, sid)
        logging.info(f"Called HTTP API for market code: {market_code}, env: {env}, buzz: {buzz}")

# 具体观察者 - 行情服务
class MarketService(Observer):
    def __init__(self, name: str):
        self.name = name
        self.sid = None

    def update(self, sid: str):
        self.sid = sid
        logging.info(f"{self.name} received new SID: {self.sid}")

    def call_http_api(self, market_code: str, env: str, buzz: dict):
        ApiCaller.call_http_api(market_code, env, buzz, self.sid)
        logging.info(f"{self.name} called HTTP API for market code: {market_code}, env: {env}, buzz: {buzz}")

# 具体观察者 - 交易服务
class TradeService(Observer):
    def __init__(self, name: str):
        self.name = name
        self.sid = None

    def update(self, sid: str):
        self.sid = sid
        logging.info(f"{self.name} received new SID: {self.sid}")

    def call_http_api(self, market_code: str, env: str, buzz: dict):
        ApiCaller.call_http_api(market_code, env, buzz, self.sid)
        logging.info(f"{self.name} called HTTP API for market code: {market_code}, env: {env}, buzz: {buzz}")

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
    market_service.call_http_api(MarketCode.vbkr.name, "prod", {"key": "value"})
    trade_service.call_http_api(MarketCode.malay.name, "prod", {"key": "value"})

    # 模拟登出
    platform_service.logout()

    # 再次尝试调用HTTP接口
    market_service.call_http_api(MarketCode.vbkr.name, "prod", {"key": "value"})
    trade_service.call_http_api(MarketCode.malay.name, "prod", {"key": "value"})
