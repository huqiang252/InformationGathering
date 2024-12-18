#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/24


def incr_by_key(d, key):
    try:
        d[key] += 1
    except KeyError:
        print(f'key {key} does not exists, re-raise the exception')
        raise