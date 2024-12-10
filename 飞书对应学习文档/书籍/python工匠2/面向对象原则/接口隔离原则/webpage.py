#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/2
# 文件名称   ：webpage.py
import datetime
from abc import ABC,abstractmethod
class HNWebPage(metaclass=ABC):

    @abstractmethod
    def get_text(self) -> str:
        """获取页面文本内容"""

    # 新增 get_size 与get_generated_at

    @abstractmethod
    def get_size(self) -> int:
        """获取页面大小"""

    @abstractmethod
    def get_generated_at(self) -> datetime.datetime:
        """获取页面生成时间"""


import requests
class RemoteHNWebPage(HNWebPage):
    """远程页面，通过请求 Hacker News 站点返回内容"""

    def __init__(self, url: str):
        self.url = url
        # 保存当前请求结果
        self._resp = None
        self._generated_at = None

    def get_text(self) -> str:
        """获取页面内容"""
        self._request_on_demand()
        return self._resp.text

    def get_size(self) -> int:
        """获取页面大小"""
        return len(self.get_text())

    def get_generated_at(self) -> datetime.datetime:
        """获取页面生成时间"""
        self._request_on_demand()
        return self._generated_at

    def _request_on_demand(self):
        """请求远程地址并避免重复"""
        if self._resp is None:
            self._resp = requests.get(self.url)
            self._generated_at = datetime.datetime.now()


class SiteAchiever:
    """将不同时间点的Hacker News 页面归档"""

    def save_page(self, page: HNWebPage):
        """将页面保存到后端数据库"""
        data = {
            "content": page.get_text(),
            "generated_at": page.get_generated_at(),
            "size": page.get_size(),
        }
        # 将 data 保存到数据库中
        # ...













