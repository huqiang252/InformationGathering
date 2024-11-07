import logging
import concurrent.futures
from deepdiff import DeepDiff
from abc import ABC, abstractmethod
import threading
from typing import  List
import requests

# 配置日志
logging.basicConfig( level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s' )


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
    def __init__(self, name: str):
        self.name = name
        self.sid = None

    def update(self, sid: str):
        self.sid = sid
        logging.info( f"{self.name} received new SID: {self.sid}" )

    def call_http_api(self, market_code: str, env: str, buzz: dict):
        host = "https://market-api.example.com"
        path = f"/api/v1/market/{market_code}"
        response = ApiCaller.call_http_api( host, path, env, buzz, self.sid )
        logging.info( f"{self.name} called HTTP API for market code: {market_code}, env: {env}, buzz: {buzz}" )
        return response


# 具体观察者 - 交易服务
class TradeService( Observer ):
    def __init__(self, name: str):
        self.name = name
        self.sid = None

    def update(self, sid: str):
        self.sid = sid
        logging.info( f"{self.name} received new SID: {self.sid}" )

    def call_http_api(self, market_code: str, env: str, buzz: dict):
        host = "https://trade-api.example.com"
        path = f"/api/v1/trade/{market_code}"
        response = ApiCaller.call_http_api( host, path, env, buzz, self.sid )
        logging.info( f"{self.name} called HTTP API for market code: {market_code}, env: {env}, buzz: {buzz}" )
        return response


# 工具类 - API 调用
class ApiCaller:
    @staticmethod
    def call_http_api(host: str, path: str, env: str, buzz: dict, sid: str):
        # 构建完整的 URL
        url = f"{host}/{path}"
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


# 示例使用
if __name__ == "__main__":
    platform_service = PlatformService()
    market_service = MarketService( "MarketService" )
    trade_service = TradeService( "TradeService" )

    platform_service.attach( market_service )
    platform_service.attach( trade_service )

    # 模拟登录
    platform_service.login( "user1", "password1" )

    # 并发请求并比较结果
    ConcurrentRequester.call_and_compare(
        market_service.call_http_api,
        (MarketCode.vbkr.name, "prod", {"key": "value"}),
        (MarketCode.vbkr.name, "uat", {"key2": "value2"})
    )

    ConcurrentRequester.call_and_compare(
        trade_service.call_http_api,
        (MarketCode.vbkr.name, "prod", {"key": "value"}),
        (MarketCode.vbkr.name, "uat", {"key2": "value2"})
    )

    # 模拟登出
    platform_service.logout()
