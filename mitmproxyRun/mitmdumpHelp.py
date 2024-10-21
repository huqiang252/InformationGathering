#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-10-20
from mitmproxy import http
from mitmproxy import ctx
import json
from typing import Any, Dict, List, Union

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

class Counter:
    def __init__(self):
        self.num = 0
        self.tradeData="2024-10-18" #定义当前日期

    def response(self,flow: http.HTTPFlow):
        request = flow.request
        response = flow.response
        info = ctx.log.info
        try:
            res = json.loads(response.get_text())  #将字符串转成字典
        except:
            res = response.get_text()
        headers = response.headers



        #获取base
        if 'base' in request.urlencoded_form:
            base=json.loads(request.urlencoded_form.get('base'))
        else:
            base=None


        #获取buzz
        if 'buzz' in request.urlencoded_form:
            buzz=json.loads(request.urlencoded_form.get('buzz'))
        else:
            buzz=None


        if request.host.endswith(".hstong.com") :
            '''涉及到权限的接口'''
            # check_json_value(res,'BMPLV2Status','LV2')
            # check_json_value(res,'USLV1Status','1')
            check_json_value(res,'mktTmType',-1)  #盘前

        if request.host.endswith(".hstong.com") and request.path in ["/hq/queryStockPreIpo"]:
            res['data'] = [{
                "securityCode": "02440.HK",
                "tradeDate": self.tradeData
            }]




        info( f'当前返回：{res}' )
        # 更改后的response
        response.set_text( json.dumps( res,
                                       ensure_ascii=False ) )  # 修改完成后，奖python对象转成json字符串，set进请求的响应体重发送给客户端;ensure_ascii:默认是True：字符之外的显示为\u4e2d\u56fd




addons = [
    Counter()
]