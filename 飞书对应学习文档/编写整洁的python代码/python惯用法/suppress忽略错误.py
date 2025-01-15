#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2025/1/12
# 文件名称   ：suppress忽略错误.py


import contextlib

with contextlib.suppress(DataConversionException):
    parse_data(input_json_or_dict)