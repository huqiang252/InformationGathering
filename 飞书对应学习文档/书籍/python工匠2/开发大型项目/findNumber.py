#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/2
# 文件名称   ：findNumber.py


import os
import re


def find_number(input_string):
    """找到字符串里的第一个整数"""
    matched_obj = re.search(r'\d+', input_sstring)
    if matched_obj:
        return int(matched_obj.group())
    return None
