#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/1
# 文件名称   ：fancylogger2.py

from logwriter import FileWriter,EsWriter,RedisWriter
class FancyLogger:
    '''日志类：支持向文件，Redis,ES等服务输出日志'''
    def __init__(self,output_writer=None):
        self._writer = output_writer or FileWriter()
        ...
    def log(self,message):
        self._writer.write(message)
