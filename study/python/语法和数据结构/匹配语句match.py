#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-07-24



'''在 Python 中，match 是 Python3.10 版本引入的一种模式匹配语法。'''


httpCode = int(input("请输入一个HTTP状态码："))

# match httpCode:
#     case 100 | 101:
#         print("临时响应")
#     case 200 | 201 | 203 | 204 | 205:
#         print("请求成功")
#     case 301 | 304 | 307:
#         print("重定向")
#     case 401 | 403| 404 | 405:
#         print("页面找不到")
#     case 500 | 502 | 503:
#         print("服务器内部错误")
#     case _:
#         print("无效的状态码")
