#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2025/1/5
# 文件名称   ：网易历史数据.py


import requests
import pandas as pd
import matplotlib.pyplot as plt


# market: 0:沪市 1:深市
# number: 股票代码
# start_data: 起始日期:yyyymmdd
# end_data: 结束时间:yyyymmdd
def getHistoryData(market, number, start_data, end_data):
    url = 'http://quotes.money.163.com/service/chddata.html?code=' + market + number + '&start=' + start_data + '&end=' + end_data
    f = open("temp.csv", "wb")
    f.write(requests.get(url).content)
    f.close()
    df = pd.read_csv('temp.csv', encoding='gbk')

    dataList = []
    for row in range(0, df.shape[0]):
        dataList.append({})
        for col in range(0, df.shape[1]):
            col_name = df.columns.values[col]
            dataList[row][col_name] = df.loc[row, col_name]

    return dataList


# col_name: 需要画的属性
def drawData(data_list, col_name):
    size = len(data_list)
    x = []
    y = []
    for i in range(size-1, -1, -1):  # 日期顺序是反的
        y.append(data_list[i][col_name])
        x.append(data_list[i]['日期'])

    plt.figure(figsize=(10, 5))
    plt.title(data_list[0]['股票代码'])
    plt.xticks([])
    plt.plot(x, y)
    plt.grid()
    plt.show()


if __name__ == '__main__':
    hisData = getHistoryData('0', '600000', '20210801', '20211203')
    print(hisData)
    drawData(hisData, '成交量')