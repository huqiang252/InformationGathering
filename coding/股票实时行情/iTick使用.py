#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2025/1/5
# 文件名称   ：iTick使用.py





import requests

url = "https://api.itick.org/indices/kline"
params = {
    "region": "gb",
    "code": "HSI",
    "kType": "1"
}
headers = {
    "accept": "application/json",
    "token": "your_api_key"
}

response = requests.get(url, params=params, headers=headers)
data = response.json()
print(data)
