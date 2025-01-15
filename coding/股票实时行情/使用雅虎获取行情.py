#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2025/1/5
# 文件名称   ：使用雅虎获取行情.py


import yfinance as yf

def get_stock_data(ticker, start_date, end_date):
    ticker_data = yf.download(ticker, start=start_date, end=end_date)
    return ticker_data

# 示例：获取苹果公司股票数据
apple_data = get_stock_data('AAPL', '2023-01-01', '2024-01-01')
print(apple_data.head())