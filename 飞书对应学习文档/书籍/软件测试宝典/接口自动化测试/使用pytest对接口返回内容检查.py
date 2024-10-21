#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-10-19

import requests,time
import pytest

def chkRsp(status_code=200):
    def chkRsp_func(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            res = func( *args, **kwargs )
            end_time = time.time()
            assert res.status_code == status_code #这里校验
        return wrapper
    return chkRsp_func


class Test_UserDBCheck():
    @chkRsp(300)
    def test_login_success(self,username='13713762959',pwd='tony137'):
        res = requests.post(
            'http://119.23.212.87:9012/login',
            json={"userName": username, "passWord": pwd}
        )
        assert res.json().get('errorCode')==""
        return res


if __name__ == '__main__':
    pytest.main(['-q'])

