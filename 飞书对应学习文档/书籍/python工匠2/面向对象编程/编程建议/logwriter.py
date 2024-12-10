#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/1
# 文件名称   ：logwriter.py




# from abc import ABC,abstractmethod
# class LogWriter(ABC):
#     @abstractmethod
#     def write(self, message):
#         ...



class FileWriter:
    def write(self, message):
        ...


class RedisWriter:
    max_length = 1024

    def write(self, message):
        message = self._pre_process(message)
        ...

    def _pre_process(self, message):
        # Redis 对日志最大长度有限制，需要进行裁剪
        return message[: self.max_length]


class EsWriter:
    def write(self, message):
        ...