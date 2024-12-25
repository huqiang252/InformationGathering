#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/14
# 文件名称   ：拦截器模式.py


# 定义Target接口
class Target:
    def request(self):
        pass


# 实现Target接口的具体类
class TargetImpl(Target):
    def request(self):
        print("TargetImpl 处理请求")


# 定义Interceptor接口
class Interceptor:
    def pre_handle(self, target):
        pass

    def post_handle(self, target):
        pass


# 实现Interceptor接口的具体类
class InterceptorImpl(Interceptor):
    def pre_handle(self, target):
        print(f"InterceptorImpl 在 {target.__class__.__name__} 前置处理")

    def post_handle(self, target):
        print(f"InterceptorImpl 在 {target.__class__.__name__} 后置处理")


# 包含了一组Interceptor和一个Target对象
class TargetInvocation:
    def __init__(self, target, interceptors=None):
        self.target = target
        self.interceptors = interceptors if interceptors else []

    def add_interceptor(self, interceptor):
        self.interceptors.append(interceptor)

    def invoke(self):
        for interceptor in self.interceptors:
            interceptor.pre_handle(self.target)

        self.target.request()

        for interceptor in reversed(self.interceptors):
            interceptor.post_handle(self.target)


# 使用示例
if __name__ == "__main__":
    target = TargetImpl()
    interceptor1 = InterceptorImpl()
    interceptor2 = InterceptorImpl()

    invocation = TargetInvocation(target)
    invocation.add_interceptor(interceptor1)
    invocation.add_interceptor(interceptor2)

    invocation.invoke()
