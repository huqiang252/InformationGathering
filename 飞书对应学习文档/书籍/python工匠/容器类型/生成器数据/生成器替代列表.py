#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/23

def batch_process(items):
    """
    批量处理多个 items 对象
    """
    # 初始化空结果列表
    results = []
    for item in items:
        # 处理 item，可能需要耗费大量时间……
        # processed_item = ...
        results.append(processed_item)
    # 将拼装后的结果列表返回
    return results



for processed_item in batch_process(items):
    # 如果某个已处理对象过期了，就中断当前的所有处理
    if processed_item.has_expired():
        break