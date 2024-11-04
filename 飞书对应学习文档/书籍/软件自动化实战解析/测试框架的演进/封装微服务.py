#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-10-28


# -- framework.common.http.QaRestClient.py --
import requests

class QaRestClient:

    @staticmethod
    def get(url):
        return requests.get(url)



# from framework.common.http.QaRestClient import QaRestClient

def test_user_service_list():
    url = 'https://jsonplaceholder.typicode.com/users'
    resp = QaRestClient.get(url)
    assert resp.status_code == 200, 'Status code not 200'
    assert len(resp.json()) > 0, 'No data returned'