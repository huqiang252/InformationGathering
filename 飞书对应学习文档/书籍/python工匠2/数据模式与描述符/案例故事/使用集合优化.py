#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/2
# 文件名称   ：使用集合优化.py


def find_potential_customers_v2():
    """ 找到去过普吉岛但是没去过新西兰的人，性能改进版"""
    # 首先，遍历所有新西兰旅客记录，创建查找索引
    nz_records_idx = {
        (rec['first_name'], rec['last_name'], rec['phone_number'])
        for rec in users_visited_nz
    }
    for rec in users_visited_puket:
        key = (rec['first_name'], rec['last_name'], rec['phone_number'])
        if key not in nz_records_idx:
            yield rec