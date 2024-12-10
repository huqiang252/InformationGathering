#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/1
# 文件名称   ：hnTopPostSpider.py


import io
import sys
from typing import Iterable, TextIO

import requests
from lxml import etree


class Post:
    """ Hacker News 上的条目

    :param title: 标题
    :param link: 链接
    :param points: 当前得分
    :param comments_cnt: 评论数
    """

    def __init__(self, title: str, link: str, points: str, comments_cnt: str):
        self.title = title
        self.link = link
        self.points = int(points)
        self.comments_cnt = int(comments_cnt)


class HNTopPostsSpider:
    """抓取 Hacker News Top 内容条目

    :param fp: 存储抓取结果的目标文件对象
    :param limit: 限制条目数，默认为 5
    """

    items_url = 'https://news.ycombinator.com/'
    file_title = 'Top news on HN'

    def __init__(self, fp: TextIO, limit: int = 5):
        self.fp = fp
        self.limit = limit

    def write_to_file(self):
        """以纯文本格式将 Hacker News Top 内容写入文件"""
        self.fp.write(f'# {self.file_title}\n\n')
        for i, post in enumerate(self.fetch(), 1):
            self.fp.write(f'> TOP {i}: {post.title}\n')
            self.fp.write(f'> 分数：{post.points} 评论数：{post.comments_cnt}\n')
            self.fp.write(f'> 地址：{post.link}\n')
            self.fp.write('------\n')

    def fetch(self) -> Iterable[Post]:
        """从Hacker News 抓取 Top 内容

        :return: 可迭代的Post 对象
        """
        resp = requests.get(self.items_url,proxies={'http': 'http://127.0.0.1:7890', 'https': 'http://127.0.0.1:7890'})

        # 使用XPath 可以方便地从页面解析出需要的内容，以下均为页面解析代码
        # 如果你对XPath 不熟悉，可以忽略这些代码，直接跳到 yield Post() 部分
        print(resp.text)
        html = etree.HTML(resp.text)

        items = html.xpath('//table[@class="itemlist"]/tr[@class="athing submission"]')
        print(f'items:{items}')
        for item in items[: self.limit]:
            node_title = item.xpath('./td[@class="title"]/a')[0]
            node_detail = item.getnext()
            points_text = node_detail.xpath('.//span[@class="score"]/text()')
            comments_text = node_detail.xpath('.//td/a[last()]/text()')[0]

            yield Post(
                title=node_title.text,
                link=node_title.get('href'),
                # 条目可能会没有评分
                points=points_text[0].split()[0] if points_text else '0',
                comments_cnt=comments_text.split()[0],
            )


if __name__== '__main__':
    from pathlib import Path
    with open(Path.cwd().joinpath('tmp','hn_top5.txt'),'w') as fp:
        crawler = HNTopPostsSpider(fp)
        crawler.write_to_file()