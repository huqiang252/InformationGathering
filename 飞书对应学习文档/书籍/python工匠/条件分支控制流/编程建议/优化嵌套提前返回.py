#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/24


def buy_fruit(nerd, store):
    if not store.is_open():
        raise MadAtNoFruit("store is closed!")

    if not store.has_stocks("apple"):
        raise MadAtNoFruit("no apple in store!")

    if nerd.can_afford(store.price("apple", amount=1)):
        nerd.buy(store, "apple", amount=1)
        return
    else:
        nerd.go_home_and_get_money()
        return buy_fruit(nerd, store)