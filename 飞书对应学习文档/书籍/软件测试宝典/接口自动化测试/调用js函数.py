#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-10-20
import execjs

def get_js():
    f = open(r'D:\test\fdLogin-3gmin.js','r',encoding='utf-8')
    line = f.readline()
    htmlstr = ""
    while line:
        htmlstr = htmlstr+line
        line = f.readline()

    return htmlstr

ctx = execjs.compile(get_js())
#调用js中hex_sha方法，对数据进行加密
print(ctx.call('hex_sha1','1234'))