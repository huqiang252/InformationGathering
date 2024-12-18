#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/2
# 文件名称   ：siteSourceCrouper.py
import requests
from typing import Dict
from collections import Counter
from xml import etree

class SiteSourceGrouper:
    """对Hacker News 新闻来源站点进行分组统计

    :param url: Hacker News 首页地址
    """

    def __init__(self, url: str):
        self.url = url

    def get_groups(self) -> Dict[str, int]:
        """获取 (域名, 个数) 分组"""
        resp = requests.get(self.url)
        html = etree.HTML(resp.text)
        # 通过 XPath 语法筛选新闻域名标签
        elems = html.xpath(
            '//table[@class="itemlist"]//span[@class="sitestr"]'
        )

        groups = Counter()
        for elem in elems:
            groups.update([elem.text])
        return groups


def main():
    groups = SiteSourceGrouper("https://news.ycombinator.com/").get_groups()
    # 打印最常见的3 个域名
    for key, value in groups.most_common(3):
        print(f'Site: {key} | Count: {value}')


if __name__ == '__main__':
    main()