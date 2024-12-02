#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/1
# 文件名称   ：get_hn_top_posts.py

import sys
from typing import Optional,TextIO
def get_hn_top_posts(fp: Optional[TextIO] = None):
    """获取 Hacker News Top 内容，并将其写入文件中

    :param fp: 需要写入的文件，如未提供，将向标准输出打印
    """
    dest_fp = fp or sys.stdout
    crawler = HNTopPostsSpider()
    writer = PostsWriter(dest_fp, title='Top news on HN')
    writer.write(list(crawler.fetch()))




class HNTopPostsSpider:
    """抓取 Hacker News Top 内容条目
    :param limit: 限制条目数，默认为 5
    :param filter_by_hosts: 过滤结果的站点列表，默认为 None，代表不过滤
    """

    def __init__(self, limit: int = 5, filter_by_hosts: Optional[List[str]] = None):
        self.limit = limit
        self.filter_by_hosts = filter_by_hosts

    def fetch(self) -> Iterable[Post]:
        counter = 0
        for item in items:
            # ...
            post = Post(...)
            # 判断链接是否符合过滤条件
            if self._check_link_from_hosts(post.link):
                counter += 1
                yield post

    def _check_link_from_hosts(self, link: str) -> True:
        """检查某链接是否属于所定义的站点"""
        if self.filter_by_hosts is None:
            return True
        parsed_link = parse.urlparse(link)
        return parsed_link.netloc in self.filter_by_hosts