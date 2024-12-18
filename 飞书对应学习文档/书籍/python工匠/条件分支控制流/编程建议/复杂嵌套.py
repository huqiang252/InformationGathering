#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/24

def buy_fruit(nerd, store):
    """去水果店买苹果操作手册：

    - 先得看看店是不是在营业
    - 如果有苹果，就买 1 个
    - 如果钱不够，就回家取钱再来
    """
    if store.is_open():
        if store.has_stocks("apple"):
            if nerd.can_afford(store.price("apple", amount=1)):
                nerd.buy(store, "apple", amount=1)
                return
            else:
                nerd.go_home_and_get_money()
                return buy_fruit(nerd, store)
        else:
            raise MadAtNoFruit("no apple in store!")
    else:
        raise MadAtNoFruit("store is closed!")