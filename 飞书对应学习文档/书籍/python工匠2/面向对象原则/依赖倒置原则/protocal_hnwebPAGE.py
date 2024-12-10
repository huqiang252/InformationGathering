#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/2
# 文件名称   ：protocal_hnwebPAGE.py

from typing import Protocol

class HNWebPage(Protocol):
    '''协议：Hacker News的站点页面'''
    def get_text(self)->str:
        ...