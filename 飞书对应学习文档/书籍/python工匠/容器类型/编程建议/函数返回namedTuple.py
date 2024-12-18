#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/24


from typing import NamedTuple


class Address(NamedTuple):
    '''地址信息结果'''
    country:str
    province:str
    city:str


def latlon_to_address(lat,lon):
    if lat > 30 and lon > 120:
        country,province,city = '中国','上海','上海'
    else:
        country,province,city = '美国','加利福尼亚','洛杉矶'
    return Address(country=country,province=province,city=city)


addr = latlon_to_address(31,121)
print(addr) #Address(country='中国', province='上海', city='上海')

print(addr.country,addr.province,addr.city)  #中国 上海 上海


addr_us = latlon_to_address(40, -120)
print(addr_us)