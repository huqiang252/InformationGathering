#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-10-20


import pytest,requests

class Test_UserDBCheck():
    @pytest.mark.flaky(reruns=2,reruns_delay=2)
    def test_login_success(self, username='13713762959', pwd='tony137'):
        print('运行开始')
        res = requests.post(
            'http://119.23.212.87:9012/login',
            json={"userName": username, "passWord": pwd}
        )
        assert res.json().get( 'errorCode' ) == "error"
        return res

if __name__ == '__main__':
    pytest.main(['-s'])
