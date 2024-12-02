#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/1
# 文件名称   ：UniqueVisitorAnalyzer3.py

from logReaderParser import LogParser,LogReader

class UniqueVisitorAnalyzer:
    """统计某日的UV 数"""
    def __init__(self, date):
        self.date = date
        self.log_reader = LogReader(self.date)
        self.log_parser = LogParser()
    def analyze(self):
        """通过解析与分析 API 访问日志，返回 UV 数
        :return: UV 数
        """
        for entry in self.get_log_entries():
            ...  # 省略：根据 entry.user_id 统计 UV 数并返回结果
    def get_log_entries(self):
        """获取当天所有日志记录"""
        for line in self.log_reader.read_lines():
            entry = self.log_parser.parse(line)
            if not self.match_news_pattern(entry.path):
                continue
            yield entry
    ...