#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/5
import logging
import concurrent.futures
from deepdiff import DeepDiff
from abc import ABC, abstractmethod
import threading
import requests
import yaml
from enum import Enum

# 配置日志
logging.basicConfig( level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s' )


# 枚举类型定义
class MarketEndpoints( Enum ):
    MARKET_DATA = "market_data"
    ORDER_BOOK = "order_book"
    # 其他接口...


class TradeEndpoints( Enum ):
    PLACE_ORDER = "place_order"
    CANCEL_ORDER = "cancel_order"
    # 其他接口...


# 配置加载器
class ConfigLoader:
    @staticmethod
    def load_config(config_file: str) -> dict:
        with open( config_file, 'r' ) as file:
            config = yaml.safe_load( file )
        return config


config = ConfigLoader.load_config( 'config.yaml' )


# 动态路由
class Router:
    def __init__(self, config: dict):
        self.config = config

    def get_base_url(self, env: str, service: str) -> str:
        return self.config['environments'][env][service]['base_url']

    def get_endpoint(self, env: str, service: str, endpoint: str) -> str:
        return self.config['environments'][env][service]['endpoints'][endpoint]


# 观察者接口
class Observer( ABC ):
    @abstractmethod
    def update(self, sid: str):
        pass


# 主题接口
class Subject( ABC ):
    def __init__(self):
        self._observers: List[Observer] = []
        self._lock = threading.Lock()

    def attach(self, observer: Observer):
        with self._lock:
            if observer not in self._observers:
                self._observers.append( observer )
                logging.info( f"Attached observer: {observer}" )

    def detach(self, observer: Observer):
        with self._lock:
            try:
                self._observers.remove( observer )
                logging.info( f"Detached observer: {observer}" )
            except ValueError:
                logging.warning( f"Observer not found: {observer}" )

    def notify(self, sid: str):
        with self._lock:
            for observer in self._observers:
                observer.update( sid )
                logging.info( f"Notified observer: {observer}" )


# 具体主题 - 平台服务
class PlatformService( Subject ):
    def __init__(self):
        super().__init__()
        self._sid = None

    @property
    def sid(self):
        return self._sid

    @sid.setter
    def sid(self, value: str):
        self._sid = value
        self.notify( value )

    def login(self, username: str, password: str) -> str:
        # 模拟登录过程
        try:
            self._sid = f"sid_{username}_{password}"
            self.notify( self._sid )  # 通知观察者
            logging.info( f"User {username} logged in successfully" )
            return self._sid
        except Exception as e:
            logging.error( f"Login failed: {e}" )
            return None

    def logout(self):
        try:
            self._sid = None
            self.notify( self._sid )  # 通知观察者
            logging.info( f"User logged out successfully" )
        except Exception as e:
            logging.error( f"Logout failed: {e}" )


# 具体观察者 - 行情服务
class MarketService( Observer ):
    def __init__(self, name: str, router: Router):
        self.name = name
        self.sid = None
        self.router = router

    def update(self, sid: str):
        self.sid = sid
        logging.info( f"{self.name} received new SID: {self.sid}" )

    def get_market_data(self, market_code: str, env: str, buzz: dict):
        return self.call_http_api( market_code, env, MarketEndpoints.MARKET_DATA, buzz )

    def get_order_book(self, market_code: str, env: str, buzz: dict):
        return self.call_http_api( market_code, env, MarketEndpoints.ORDER_BOOK, buzz )

    def call_http_api(self, market_code: str, env: str, endpoint: MarketEndpoints, buzz: dict):
        base_url = self.router.get_base_url( env, "market" )
        path = self.router.get_endpoint( env, "market", endpoint.value ).format( market_code=market_code )
        response = ApiCaller.call_http_api( base_url, path, env, buzz, self.sid )
        logging.info( f"{self.name} called HTTP API for market code: {market_code}, env: {env}, endpoint: {endpoint.value}, buzz: {buzz}" )
        return response


# 具体观察者 - 交易服务
class TradeService( Observer ):
    def __init__(self, name: str, router: Router):
        self.name = name
        self.sid = None
        self.router = router

    def update(self, sid: str):
        self.sid = sid
        logging.info( f"{self.name} received new SID: {self.sid}" )

    def place_order(self, market_code: str, env: str, buzz: dict):
        return self.call_http_api( market_code, env, TradeEndpoints.PLACE_ORDER, buzz )

    def cancel_order(self, market_code: str, env: str, buzz: dict):
        return self.call_http_api( market_code, env, TradeEndpoints.CANCEL_ORDER, buzz )

    def call_http_api(self, market_code: str, env: str, endpoint: TradeEndpoints, buzz: dict):
        base_url = self.router.get_base_url( env, "trade" )
        path = self.router.get_endpoint( env, "trade", endpoint.value ).format( market_code=market_code )
        response = ApiCaller.call_http_api( base_url, path, env, buzz, self.sid )
        logging.info( f"{self.name} called HTTP API for market code: {market_code}, env: {env}, endpoint: {endpoint.value}, buzz: {buzz}" )
        return response


# 工具类 - API 调用
class ApiCaller:
    @staticmethod
    def call_http_api(base_url: str, path: str, env: str, buzz: dict, sid: str):
        # 构建完整的 URL
        url = f"{base_url}{path}"
        headers = {
            "Authorization": f"Bearer {sid}",
            "Content-Type": "application/json"
        }
        params = {**buzz, "env": env}

        # 发送 HTTP GET 请求
        response = requests.get( url, headers=headers, params=params )
        response.raise_for_status()  # 抛出异常，如果响应状态码不是 200
        return response.json()


# 通用并发请求和结果比较工具类
class ConcurrentRequester:
    @staticmethod
    def call_and_compare(request_func, *args_list):
        """
        并发调用请求函数并比较结果。

        :param request_func: 请求函数，接受 *args 作为参数
        :param args_list: 每个请求的参数列表，每个元素是一个元组
        :return: 比较结果
        """
        results = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit( request_func, *args ) for args in args_list]

            for future in concurrent.futures.as_completed( futures ):
                try:
                    result = future.result()
                    results.append( result )
                except Exception as e:
                    logging.error( f"Request failed: {e}" )
                    results.append( None )

        # 比较结果
        if len( results ) < 2:
            logging.warning( "Not enough results to compare" )
            return None

        diff = DeepDiff( results[0], results[1] )
        if diff:
            logging.warning( f"Differences found between results: {diff}" )
        else:
            logging.info( "No differences found between results" )

        return diff


if __name__ == "__main__":
    router = Router( config )

    platform_service = PlatformService()
    market_service = MarketService( "Market Service", router )
    trade_service = TradeService( "Trade Service", router )

    platform_service.attach( market_service )
    platform_service.attach( trade_service )

    sid = platform_service.login( "user1", "password1" )

    if sid:
        # 获取市场数据
        market_data = market_service.get_market_data( "BTCUSD", "prod", {"param1": "value1"} )
        print( market_data )

        # 下单
        order_result = trade_service.place_order( "BTCUSD", "prod", {"amount": 1.0, "price": 20000.0} )
        print( order_result )

        # 注销
        platform_service.logout()