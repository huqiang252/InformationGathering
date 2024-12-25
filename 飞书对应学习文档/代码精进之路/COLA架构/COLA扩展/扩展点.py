#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/17
# 文件名称   ：扩展点.py


# 定义业务身份
class BizCode:
    ALI_TMAILL = "ali.tmall"
    ALI_TMAILL_CAR = "ali.tmall.car"
    ALI_TMAILL_CAR_AFTERSALE = "ali.tmall.car.aftermarket"

# 定义扩展点接口
class ExtensionPoint:
    def execute(self):
        raise NotImplementedError("This method should be implemented by subclasses")

# 支付扩展点
class PaymentExtension(ExtensionPoint):
    def execute(self):
        print("Executing payment extension")

# 物流扩展点
class ShippingExtension(ExtensionPoint):
    def execute(self):
        print("Executing shipping extension")

# 客户服务扩展点
class CustomerServiceExtension(ExtensionPoint):
    def execute(self):
        print("Executing customer service extension")

# 扩展坐标管理
class ExtensionManager:
    def __init__(self):
        self.extensions = {}

    def register_extension(self, biz_code: str, extension_point: str, extension: ExtensionPoint):
        key = f"{biz_code}.{extension_point}"
        self.extensions[key] = extension

    def get_extension(self, biz_code: str, extension_point: str) -> ExtensionPoint:
        key = f"{biz_code}.{extension_point}"
        return self.extensions.get(key)

# 注册扩展实现
manager = ExtensionManager()
manager.register_extension(BizCode.ALI_TMAILL_CAR, "payment", PaymentExtension())
manager.register_extension(BizCode.ALI_TMAILL_CAR, "shipping", ShippingExtension())
manager.register_extension(BizCode.ALI_TMAILL_CAR, "customerService", CustomerServiceExtension())

# 查找并调用扩展
payment_extension = manager.get_extension(BizCode.ALI_TMAILL_CAR, "payment")
if payment_extension:
    payment_extension.execute()

shipping_extension = manager.get_extension(BizCode.ALI_TMAILL_CAR, "shipping")
if shipping_extension:
    shipping_extension.execute()

customer_service_extension = manager.get_extension(BizCode.ALI_TMAILL_CAR, "customerService")
if customer_service_extension:
    customer_service_extension.execute()
