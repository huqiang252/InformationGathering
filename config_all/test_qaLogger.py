#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/22
# 文件名称   ：test_qaLogger.py


from config_all.qaLogger import QaLogger
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