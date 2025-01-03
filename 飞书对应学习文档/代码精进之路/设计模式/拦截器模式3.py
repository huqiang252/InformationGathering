#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/14
# 文件名称   ：拦截器模式3.py

import logging
import requests
from abc import ABC, abstractmethod

# 配置日志
logging.basicConfig(level=logging.INFO)

# 定义Target接口
class Target(ABC):
    @abstractmethod
    def request(self, method, url, **kwargs):
        pass

# 实现Target接口的具体类
class HttpTarget(Target):
    def request(self, method, url, **kwargs):
        response = requests.request(method, url, **kwargs)
        logging.info(f"HttpTarget 处理请求: {method} {url}, 响应状态码: {response.status_code}")
        return response

# 定义Interceptor接口
class Interceptor(ABC):
    @abstractmethod
    def pre_handle(self, method, url, kwargs):
        pass

    @abstractmethod
    def post_handle(self, response):
        pass

# 实现Interceptor接口的具体类 - 日志记录
class LoggingInterceptor(Interceptor):
    def pre_handle(self, method, url, kwargs):
        logging.info(f"LoggingInterceptor 在 {method} {url} 前置处理")

    def post_handle(self, response):
        logging.info(f"LoggingInterceptor 在 {response.status_code} 后置处理")

# 实现Interceptor接口的具体类 - 认证
class AuthInterceptor(Interceptor):
    def __init__(self, token):
        self.token = token

    def pre_handle(self, method, url, kwargs):
        headers = kwargs.get('headers', {})
        headers['Authorization'] = f'Bearer {self.token}'
        kwargs['headers'] = headers
        logging.info(f"AuthInterceptor 在 {method} {url} 前置处理 - 添加认证头")

    def post_handle(self, response):
        logging.info(f"AuthInterceptor 在 {response.status_code} 后置处理")

# 实现Interceptor接口的具体类 - 性能监控
class PerformanceInterceptor(Interceptor):
    def pre_handle(self, method, url, kwargs):
        self.start_time = time.time()
        logging.info(f"PerformanceInterceptor 在 {method} {url} 前置处理 - 开始计时")

    def post_handle(self, response):
        elapsed_time = time.time() - self.start_time
        logging.info(f"PerformanceInterceptor 在 {response.status_code} 后置处理 - 响应时间: {elapsed_time:.2f} 秒")

# 包含了一组Interceptor和一个Target对象
class TargetInvocation:
    def __init__(self, target, interceptors=None):
        self.target = target
        self.interceptors = interceptors if interceptors else []

    def add_interceptor(self, interceptor):
        self.interceptors.append(interceptor)

    def invoke(self, method, url, **kwargs):
        try:
            for interceptor in self.interceptors:
                interceptor.pre_handle(method, url, kwargs)

            response = self.target.request(method, url, **kwargs)

            for interceptor in reversed(self.interceptors):
                interceptor.post_handle(response)

            return response
        except Exception as e:
            logging.error(f"请求处理过程中发生错误: {e}")
            raise

# 使用示例
if __name__ == "__main__":
    import time

    target = HttpTarget()
    logging_interceptor = LoggingInterceptor()
    auth_interceptor = AuthInterceptor(token="your_token_here")
    performance_interceptor = PerformanceInterceptor()

    invocation = TargetInvocation(target)
    invocation.add_interceptor(logging_interceptor)
    invocation.add_interceptor(auth_interceptor)
    invocation.add_interceptor(performance_interceptor)

    response = invocation.invoke('GET', 'https://hqr.hstong.com/hs/definition/definitionNew.json')
    # print(response.json())

