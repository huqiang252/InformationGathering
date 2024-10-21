#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-10-19


import requests, time


# 定义一个装饰器，用来处理统一的测试检查过程
def chkRsp(status_code=200,errorCode=''):
    def chkRsp_func(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            res = func( *args, **kwargs )
            end_time = time.time()
            if res.status_code == status_code:
                print( f'{res.url}..success..耗时：{end_time - start_time}秒' )
            else:
                print( f'{res.url}..fail..耗时：{end_time - start_time}秒' )
        return wrapper
    return chkRsp_func


class RouteAPITest():
    # 处理用户信息的接口测试
    def __init__(self):
        self._username = '13713762959'
        self._password = ""
        self._token = None
        self._openId = None

    ##外部对象，可读，可设置username,password
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value


    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @chkRsp(status_code=200)
    def test_login(self):
        print('开始执行登录方法')
        res = requests.post(
            'http://119.23.212.87:9012/login',
            json={"userName": self._username, "passWord": self._password}
        )

        self._token = res.json().get( 'data' ).get( 'token' )
        self._openId = res.json().get( 'data' ).get( 'openId' )
        print(res.json())
        return res

    @chkRsp()
    def test_totalHtml(self):
        print('获取列表html内容')
        res = requests.get( 'http://119.23.212.87:9012/totalHtml?',
                             params={'token': self._token, 'openId': self._openId} )
        return res

    @chkRsp()
    def test_index(self):
        print('获取主页内容')
        res = requests.get('http://119.23.212.87:9012/index?',
                            params={'token': self._token, 'openId': self._openId})
        return res


if __name__ == '__main__':
    route = RouteAPITest()
    route.username = '13713762959'
    route.password = 'tony137'

    # 调用，执行所有test方法
    for func in route.__dir__():
        if 'test_' in func and hasattr(route,func):
            getattr(route,func)()

    # [getattr(route,func)() for func in route.__dir__() if 'test_' in func and hasattr(route,func)]