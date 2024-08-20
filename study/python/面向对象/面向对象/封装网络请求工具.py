#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-07-27
class RequestTools(object):
    @classmethod
    def get(cls, url, header, callback):
        callback(url, header)

    @classmethod
    def post(cls, url, header, callback):
        callback(url, header)

    @classmethod
    def put(cls, url, header, callback):
        callback(url, header)

    @classmethod
    def delete(cls, url, header, callback):
        callback(url, header)


def func(url, header):
    print(f"请求的网址是 {url}")
    print(f"请求的信息有 ：")
    for i in header:
        print(i,header[i])

if __name__ == '__main__':

    RequestTools.get('http://www.baidu.com', {"content-type":"text/html"}, func)
    RequestTools.post('http://www.baidu.com', {"content-type":"text/html"}, func)
    RequestTools.put('http://www.baidu.com', {"content-type":"text/html"}, func)
    RequestTools.delete('http://www.baidu.com', {"content-type":"text/html"}, func)
