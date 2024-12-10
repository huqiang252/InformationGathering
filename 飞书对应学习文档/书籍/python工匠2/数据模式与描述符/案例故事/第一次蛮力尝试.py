#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/2
# 文件名称   ：第一次蛮力尝试.py



def find_potential_customers_v1():
    """找到去过普吉岛但是没去过新西兰的人
    :return: 通过 Generator 返回符合条件的旅客记录
    """
    for puket_record in users_visited_puket:
        is_potential = True
        for nz_record in users_visited_nz:
            if (
                puket_record['first_name'] == nz_record['first_name']
                and puket_record['last_name'] == nz_record['last_name']
                and puket_record['phone_number'] == nz_record['phone_number']
            ):
                is_potential = False
                break
        if is_potential:
            yield puket_record