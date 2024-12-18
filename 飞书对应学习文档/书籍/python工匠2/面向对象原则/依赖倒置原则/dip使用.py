#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/2
# 文件名称   ：dip使用.py


from abc import ABC,abstractmethod

class HNWebPage(ABC):
    @abstractmethod
    def get_text(self)->str:
        raise NotImplementedError()

import requests
class RemoteHNWebPage(HNWebPage):
    def __init__(self,url:str):
        self.url = url
    def get_text(self)->str:
        resp = requests.get(self.url)
        return resp.text

class LocalHNWebPage(HNWebPage):
    """本地页面，根据本地文件返回页面内容

    :param path: 本地文件路径
    """

    def __init__(self, path: str):
        self.path = path

    def get_text(self) -> str:
        with open(self.path, 'r') as fp:
            return fp.read()


from xml import etree
from typing import Dict
class SiteSourceGrouper:
    """对Hacker News 页面的新闻来源站点进行分组统计"""

    def __init__(self, page: HNWebPage):
        self.page = page

    def get_groups(self) -> Dict[str, int]:
        """获取 (域名, 个数) 分组"""
        html = etree.HTML(self.page.get_text())
        ...

def main():
    page = RemoteHNWebPage(url="https://news.ycombinator.com/")
    grouper = SiteSourceGrouper(page).get_groups()


