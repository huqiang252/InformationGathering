#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-07-28


import sys
# 第一个元素是脚本名称，后续元素是命令行参数
script_name = sys.argv[0]
arguments = sys.argv[1:]

print("脚本名称：", script_name)
print("命令行参数：", arguments)

print("Python 解释器版本：", sys.version)
print("Python 解释器版本信息：", sys.version_info)
print("当前操作系统平台：", sys.platform)
for module_name, module in sys.modules.items():
    print(f"模块名：{module_name}, 模块对象：{module}")

print(f'解释器搜索模块的路径:{sys.path}')  #用于指定 Python 解释器搜索模块的路径。
# 获取系统当前编码
print(sys.getdefaultencoding())
