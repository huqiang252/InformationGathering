#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2025/1/5
# 文件名称   ：使用新浪获取实时行情数据.py


import requests


# market: sh:沪市 sz:深市
# number: 股票代码
def getData(market, number):
    url = 'http://hq.sinajs.cn/list=' + market + number
    respond = requests.get(url)
    index = respond.text.find('=') + 2
    data_arr = respond.text[index:-4].split(',')
    # print(data_arr)
    data = {'股票代码': data_arr[0], '今日开盘价': data_arr[1], '昨日收盘价': data_arr[2], '当前价格': data_arr[3], '今日最高价': data_arr[4],
            '今日最低价': data_arr[5], '竞买价': data_arr[6], '竞卖价': data_arr[7], '成交的股票数': data_arr[8], '成交金额': data_arr[9],
            '买一挂单': data_arr[10], '买一报价': data_arr[11], '买二挂单': data_arr[12], '买二报价': data_arr[13],
            '买三挂单': data_arr[14], '买三报价': data_arr[15], '买四挂单': data_arr[16], '买四报价': data_arr[17],
            '买五挂单': data_arr[18], '买五报价': data_arr[19], '卖一挂单': data_arr[20], '卖一报价': data_arr[21],
            '卖二挂单': data_arr[22], '卖二报价': data_arr[23], '卖三挂单': data_arr[24], '卖三报价': data_arr[25],
            '卖四挂单': data_arr[26], '卖四报价': data_arr[27], '卖五挂单': data_arr[28], '卖五报价': data_arr[29],
            '日期': data_arr[30], '时间': data_arr[31]}

    return data


if __name__ == '__main__':
    realTimeData = getData('sh', '600000')
    print(realTimeData)