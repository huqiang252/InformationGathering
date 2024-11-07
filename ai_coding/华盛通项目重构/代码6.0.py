#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/6

from abc import ABC, abstractmethod
import requests
import socket

# 抽象接口层
class HttpClient(ABC):
    @abstractmethod
    def send_request(self, url, method, data):
        pass

# 具体实现
class RequestsClient(HttpClient):
    def send_request(self, url, method, data):
        response = requests.request(method, url, json=data)
        return response.json()

class SocketClient(HttpClient):
    def send_request(self, url, method, data):
        # 假设这里实现了通过socket发送HTTP请求的逻辑
        # 这里只是一个示例，实际实现会更复杂
        return {"status": "success"}

# 工厂模式
class HttpClientFactory:
    @staticmethod
    def get_client(client_type):
        if client_type == 'requests':
            return RequestsClient()
        elif client_type == 'socket':
            return SocketClient()
        else:
            raise ValueError("Unknown client type")

# 单例模式
class ConfigManager:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(ConfigManager, cls).__new__(cls)
            cls._instance.config = {}
        return cls._instance

    def set_config(self, key, value):
        self.config[key] = value

    def get_config(self, key):
        return self.config.get(key)

# 装饰器模式
class LoggingDecorator(HttpClient):
    def __init__(self, client):
        self.client = client

    def send_request(self, url, method, data):
        print(f"Sending {method} request to {url} with data: {data}")
        response = self.client.send_request(url, method, data)
        print(f"Response received: {response}")
        return response

# 测试用例
def test_http_client():
    config_manager = ConfigManager()
    config_manager.set_config('client_type', 'requests')

    client_type = config_manager.get_config('client_type')
    client = HttpClientFactory.get_client(client_type)
    logging_client = LoggingDecorator(client)

    url = "https://api.example.com/data"
    method = "POST"
    data = {"key": "value"}

    response = logging_client.send_request(url, method, data)
    assert response["status"] == "success"

if __name__ == "__main__":
    test_http_client()
