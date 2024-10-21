#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-10-19

import time
import pytest
@pytest.fixture()
def postCode():
    return '0000'


@pytest.fixture()
def db():
    '''用来模拟数据库的链接，关闭'''
    print('数据库 链接成功')
    yield
    print('数据库 关闭')


@pytest.fixture(autouse=True)
def time_funtion_scope():
    start = time.time()
    yield
    print(f'函数花费时间：{time.time()-start}s')