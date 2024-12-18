#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/2
# 文件名称   ：分拆接口.py
import datetime
from abc import ABC,abstractmethod
class ContentOnlyHNWebPage(ABC):
    """ 抽象类：Hacker News 站点页面（仅提供内容）"""

    @abstractmethod
    def get_text(self) -> str:
        raise NotImplementedError()


class HNWebPage(ABC):
    """ 抽象类：Hacker New 站点页面（含元数据）"""

    @abstractmethod
    def get_text(self) -> str:
        raise NotImplementedError()

    @abstractmethod
    def get_size(self) -> int:
        """ 获取页面大小"""
        raise NotImplementedError()

    @abstractmethod
    def get_generated_at(self) -> datetime.datetime:
        """ 获取页面生成时间"""
        raise NotImplementedError()