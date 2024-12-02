#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/1
# 文件名称   ：UniqueVisitorAnalyzer2.py
import re
class UniqueVisitorAnalyzer:


    def __init__(self, date):
        self.date = date

    def analyze(self):
        """通过解析与分析 API 访问日志，返回 UV 数

        :return: UV 数
        """
        for entry in self.get_log_entries():
            ... # 省略：根据 entry.user_id 统计 UV 数并返回结果

    def get_log_entries(self):
        """获取当天所有日志记录"""
        for line in self.read_log_lines():
            entry = self.parse_log(line)
            if not self.match_news_pattern(entry.path):
                continue
            yield entry
    def match_news_pattern(self, path):
        """判断 API 路径是不是在访问新闻
        :param path: API 访问路径
        :return: bool
        """
        return re.match(r'^/news/[^/]*?/$', path)


    def read_log_lines(self):
        """逐行获取访问日志"""
        ...  # 省略：根据日志 self.date 读取日志文件并返回结果


    def parse_log(self, line):
        """将纯文本格式的日志解析为结构化对象

        :param line: 纯文本格式日志
        :return: 结构化的日志条目 LogEntry 对象
        """
        ...  # 省略：复杂的日志解析过程
        return LogEntry(
            time=...,
            ip=...,
            path=...,
            user_agent=...,
            user_id=...,
        )


class Top10CommentsAnalyzer(UniqueVisitorAnalyzer):
    def analyze(self):
        # 当小 V 修改了父类 UniqueVisitorAnalyzer 的
        # get_log_entries() 方法后，子类的get_log_entries()
        # 方法调用从此只能拿到路径属于"查看新闻"的日志条目
        for entry in self.get_log_entries():
            comment_id = self.extract_comment_id(entry.path)
            ...
    def extract_comment_id(self, path):
        # 因为输入源发生了变化，所以extract_comment_id() 永远匹配不到
        # 任何点赞评论的路径了
        matched_obj = re.match('/comments/(.*)/up_votes/', path)
        return matched_obj and matched_obj.group(1)