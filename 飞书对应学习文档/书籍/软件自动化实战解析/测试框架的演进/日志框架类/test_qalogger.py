#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/29
from Qalogger import  QaLogger

logger = QaLogger()

def test_put_new_order():
    logger.step('login...')
    # app.home.login()
    print('app 已经登录')
    logger.step_done()

    logger.step('close wizard...')
    # app.wizard.close()
    print('app 关闭窗口了')
    logger.step_done()

    logger.step('put new order')
    # app.order.create_new_order()
    print('app 创建一个新页面')
    logger.step_done()

    ...