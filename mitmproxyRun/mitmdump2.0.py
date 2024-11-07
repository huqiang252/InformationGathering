from mitmproxy import http
from mitmproxy import ctx
import json
from typing import Any, Dict, List, Union

# 辅助函数
def check_json_value(dic_json: Union[Dict[str, Any], List[Any]], k: str, v: Any) -> Union[Dict[str, Any], List[Any]]:
    '''对json文件的k键替换对应的新value'''
    if isinstance(dic_json, dict):
        for key, value in dic_json.items():
            if key == k:
                dic_json[key] = v
            elif isinstance(value, (dict, list)):
                check_json_value(value, k, v)
    elif isinstance(dic_json, list):
        for item in dic_json:
            if isinstance(item, (dict, list)):
                check_json_value(item, k, v)
    return dic_json

# 策略模式
class ResponseHandler:
    def __init__(self):
        self.strategies = []

    def add_strategy(self, strategy):
        self.strategies.append(strategy)

    def handle_response(self, flow: http.HTTPFlow):
        request = flow.request
        response = flow.response
        info = ctx.log.info

        try:
            res = json.loads(response.get_text())  # 将字符串转成字典
        except json.JSONDecodeError as e:
            info(f"JSON解码错误: {e}")
            res = response.get_text()

        if not res:
            info("响应内容为空")
            return

        if not isinstance(res, dict):
            info("响应内容不是字典类型")
            return

        for strategy in self.strategies:
            if strategy.matches(request):
                res = strategy.apply(res)

        info(f'当前返回：{res}')
        response.set_text(json.dumps(res, ensure_ascii=False))  # 修改完成后，将Python对象转成JSON字符串，set进请求的响应体中发送给客户端

# 具体策略类
class PermissionStrategy:
    def matches(self, request: http.Request) -> bool:
        return request.host.endswith(".hstong.com")

    def apply(self, res: Dict[str, Any]) -> Dict[str, Any]:
        check_json_value(res, 'mktTmType', -1)  # 盘前
        return res

class QueryStockPreIpoStrategy:
    def __init__(self, trade_data: str):
        self.trade_data = trade_data

    def matches(self, request: http.Request) -> bool:
        return request.host.endswith(".hstong.com") and request.path in ["/hq/queryStockPreIpo"]

    def apply(self, res: Dict[str, Any]) -> Dict[str, Any]:
        res['data'] = [{
            "securityCode": "02440.HK",
            "tradeDate": self.trade_data
        }]
        return res

# 主类
class Counter:
    def __init__(self):
        self.num = 0
        self.tradeData = "2024-10-18"  # 定义当前日期
        self.handler = ResponseHandler()
        self.register_strategies()

    def register_strategies(self):
        self.handler.add_strategy(PermissionStrategy())
        self.handler.add_strategy(QueryStockPreIpoStrategy(self.tradeData))

    def response(self, flow: http.HTTPFlow):
        self.handler.handle_response(flow)

# 注册插件
addons = [
    Counter()
]
