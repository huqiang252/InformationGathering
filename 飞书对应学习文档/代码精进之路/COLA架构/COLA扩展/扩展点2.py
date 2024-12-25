class BizCode:
    """ 业务身份类 """
    def __init__(self, biz_code: str):
        self.biz_code = biz_code

    def __str__(self):
        return self.biz_code

    def __eq__(self, other):
        if isinstance(other, BizCode):
            return self.biz_code == other.biz_code
        return False

    def __hash__(self):
        return hash(self.biz_code)

# 定义具体的业务身份
ALI_TMALL_PAYMENT = BizCode("ali.tmall.payment")
ALI_TMALL_CAR_AFTERMARKET = BizCode("ali.tmall.car.aftermarket")

class ExtensionPoint:
    """ 扩展点基类 """
    def execute(self):
        raise NotImplementedError("This method should be overridden by subclasses")

class PaymentExtensionPoint(ExtensionPoint):
    """ 支付扩展点 """
    def execute(self):
        raise NotImplementedError("This method should be overridden by subclasses")

class AlipayExtension(PaymentExtensionPoint):
    """ 支付宝支付扩展实现 """
    def execute(self):
        print("Processing payment via Alipay")

class WeChatPayExtension(PaymentExtensionPoint):
    """ 微信支付扩展实现 """
    def execute(self):
        print("Processing payment via WeChat Pay")

def get_extension(biz_code: BizCode, extension_point_type: type) -> ExtensionPoint:
    """ 根据业务身份和扩展点类型获取对应的扩展实现 """
    if biz_code == ALI_TMALL_PAYMENT and issubclass(extension_point_type, PaymentExtensionPoint):
        if extension_point_type is AlipayExtension:
            return AlipayExtension()
        elif extension_point_type is WeChatPayExtension:
            return WeChatPayExtension()
    else:
        raise ValueError("No matching extension found")

# 使用示例
biz_code = ALI_TMALL_PAYMENT
extension_point_type = AlipayExtension
extension = get_extension(biz_code, extension_point_type)
extension.execute()
