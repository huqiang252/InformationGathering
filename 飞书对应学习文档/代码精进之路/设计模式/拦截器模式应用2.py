#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/14
# 文件名称   ：拦截器模式应用2.py


import logging

# 配置日志
logging.basicConfig(level=logging.INFO)

# 定义Target接口
class Target:
    def request(self):
        pass

# 实现Target接口的具体类
class TargetImpl(Target):
    def request(self):
        logging.info("TargetImpl 处理请求")
        print("TargetImpl 处理请求")

# 定义Interceptor接口
class Interceptor:
    def pre_handle(self, target):
        pass

    def post_handle(self, target):
        pass

# 实现Interceptor接口的具体类 - 权限检查
class PermissionInterceptor(Interceptor):
    def pre_handle(self, target):
        user_role = "admin"  # 假设这是从某个地方获取的用户角色
        if user_role != "admin":
            raise PermissionError("用户没有权限执行此操作")
        logging.info("PermissionInterceptor 前置处理 - 权限检查通过")

    def post_handle(self, target):
        logging.info("PermissionInterceptor 后置处理")

# 实现Interceptor接口的具体类 - 日志记录
class LoggingInterceptor(Interceptor):
    def pre_handle(self, target):
        logging.info(f"LoggingInterceptor 在 {target.__class__.__name__} 前置处理")

    def post_handle(self, target):
        logging.info(f"LoggingInterceptor 在 {target.__class__.__name__} 后置处理")

# 包含了一组Interceptor和一个Target对象
class TargetInvocation:
    def __init__(self, target, interceptors=None):
        self.target = target
        self.interceptors = interceptors if interceptors else []

    def add_interceptor(self, interceptor):
        self.interceptors.append(interceptor)

    def invoke(self):
        try:
            for interceptor in self.interceptors:
                interceptor.pre_handle(self.target)

            self.target.request()

            for interceptor in reversed(self.interceptors):
                interceptor.post_handle(self.target)
        except Exception as e:
            logging.error(f"请求处理过程中发生错误: {e}")
            raise

# 使用示例
if __name__ == "__main__":
    target = TargetImpl()
    permission_interceptor = PermissionInterceptor()
    logging_interceptor = LoggingInterceptor()

    invocation = TargetInvocation(target)
    invocation.add_interceptor(permission_interceptor)
    invocation.add_interceptor(logging_interceptor)

    invocation.invoke()
