#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/1
# 文件名称   ：fancylogger.py

from enum import Enum
class OutputType(Enum,str):
    """日志输出类型"""
    FILE = 'file'
    REDIS = 'redis'
    ES = 'es'

class FancyLogger:
    """日志类：支持向文件、Redis、ES 等服务输出日志"""

    _redis_max_length = 1024

    def __init__(self, output_type=OutputType.FILE):
        self.output_type = output_type
        ...

    def log(self, message):
        """打印日志"""
        if self.output_type == OutputType.FILE:
            ...
        elif self.output_type == OutputType.REDIS:
            ...
        elif self.output_type == OutputType.ES:
            ...
        else:
            raise TypeError('output type invalid')

    def pre_process(self, message):
        """预处理日志"""
        # Redis 对日志最大长度有限制，需要进行裁剪
        if self.output_type == OutputType.REDIS:
            return message[: self._redis_max_length]