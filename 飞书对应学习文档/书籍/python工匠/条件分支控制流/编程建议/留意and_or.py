#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/24 


context = {}
# 仅当 extra_context 不为 None 时，将其追加进 context 中
if extra_context:
    context.update(extra_context)