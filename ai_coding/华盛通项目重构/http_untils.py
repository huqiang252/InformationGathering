#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/4
import json
import uuid
import time
import requests
from enum import Enum

# 假设这些是你的加密和签名函数
def data_encrpt(data: str) -> str:
    # 模拟数据加密
    return data

def data_sign(market_code: str, data: dict) -> dict:
    # 模拟数据签名
    signed_data = data.copy()
    signed_data["sign"] = "signed_data"
    return signed_data

class MarketCode(Enum):
    vbkr = "vbkr"
    malay = "malay"
    sg = "sg"

class Lang(Enum):
    zh_CN = "zh_CN"
    en_US = "en_US"

class HttpUtils:
    @staticmethod
    def hst_post_data(
        market_code: str,
        env: str,
        buzz: dict,
        sid: str = "",
        lang: str = "",
        version: str = "",
        url: str = "https://example.com/api"
    ) -> dict:
        if market_code == MarketCode.vbkr.name:
            base = {
                "agentId": "100000",
                "appType": "1",
                "clientType": "1",
                "env": env,
                "ext1": data_encrpt("imei"),
                "imei": data_encrpt("imei"),
                "iv": "2",
                "lang": lang if lang else Lang.zh_CN.value,
                "macAdrs": "",
                "noncestr": str(uuid.uuid4()).replace("-", ""),
                "theme": "light",
                "timestamp": str(round(time.time() * 1000)),
                "version": version if version else "2.7.610"
            }

        elif market_code == MarketCode.malay.name:
            base = {
                "agentId": "1110904",
                "appType": "11",
                "clientType": "1",
                "env": env,
                "imei": "imei",
                "lang": lang if lang else Lang.zh_CN.value,
                "noncestr": str(time.time()).replace(".", "")[:11],
                "theme": "light",
                "timeZone": "Asia/Shanghai",
                "timestamp": str(round(time.time() * 1000)),
                "version": version if version else '4.2.0',
                "saltVersion": "1"
            }

        elif market_code == MarketCode.sg.name:
            base = {
                "agentId": "1110002",
                "appType": "10",
                "clientType": "1",
                "env": env,
                "imei": "imei",
                "lang": lang if lang else Lang.en_US.value,
                "noncestr": str(uuid.uuid4()).replace("-", ""),
                "theme": "light",
                "timeZone": "Asia/Shanghai",
                "timestamp": str(round(time.time() * 1000)),
                "version": version if version else '2.7.0'
            }

        if sid:
            base['sid'] = sid

        data = data_sign(market_code, {
            "base": json.dumps(base),
            'buzz': json.dumps(buzz),
            "format": "json",
            "sign": ""
        })

        response = requests.post(url, json=data)
        response.raise_for_status()  # 抛出HTTP错误
        return response.json()

    @staticmethod
    def call_http_api(market_code: str, env: str, buzz: dict, sid: str = "", lang: str = "", version: str = "", url: str = "https://example.com/api"):
        try:
            response_data = HttpUtils.hst_post_data(market_code, env, buzz, sid, lang, version, url)
            print(f"HTTP API response: {response_data}")
            return response_data
        except requests.RequestException as e:
            print(f"HTTP request failed: {e}")
            return None
