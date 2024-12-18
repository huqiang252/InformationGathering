#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/1
# 文件名称   ：top10CommentsAnalyzer.py


from logReaderParser import LogReader,LogParser
class Top10CommentsAnalyzer:
    """获取某日点赞量最高的10 条评论"""
    limit = 10
    def __init__(self, date):
        self.log_reader = LogReader(self.date)
        self.log_parser = LogParser()
    ...
    def get_log_entries(self):
        for line in self.log_reader.read_lines():
            entry = self.log_parser.parse(line)
            yield entry