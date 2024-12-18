#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/25


class CreateItemError(Exception):
    """创建 Item 失败

    :param error_code: 错误代码
    :param message: 错误信息
    """

    def __init__(self, error_code, message):
        self.error_code = error_code
        self.message = message
        super().__init__(f'{self.error_code} - {self.message}')


# 抛出异常时指定 error_code
# raise CreateItemError('name_too_long', 'name of item is too long')
raise CreateItemError('items_full', 'items is full')