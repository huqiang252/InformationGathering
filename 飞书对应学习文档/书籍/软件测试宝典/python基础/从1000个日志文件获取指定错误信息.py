#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-10-19


import os


#文件路径
dirPath = r"C:\Users\qiang.hu\AppData\Roaming\OpenAPIGateway\logs"
for filename in os.listdir(dirPath):
    with open(dirPath+"\\"+filename,encoding='utf-8') as f:
        #获取文件中的每个文本
        for row in f.readlines():
            #如果某一行文本信息，存在则输出就行
            if "异常" in row:
                print(row)