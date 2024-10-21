#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-10-19


import requests
from logbook的使用 import log
#步骤1：初始数据


#步骤2：参数构造
url = 'http://119.23.212.87:9012/login'
data = {"userName":"13713762959","passWord":"tony137"}


#步骤3：发送请求
response = requests.post(url,json=data)
log.info(response.text)

#步骤4：断言
if response.status_code==200 and response.json().get('errorCode')=='':
    log.info('success')
else:
    log.info('fail')