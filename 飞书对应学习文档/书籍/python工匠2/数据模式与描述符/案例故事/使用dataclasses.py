#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/2
# 文件名称   ：使用dataclasses.py


from dataclasses import dataclass, field
@dataclass(frozen=True)
class VisitRecordDC:
    first_name: str
    last_name: str
    phone_number: str
    date_visited: str = field(compare=False)

def find_potential_customers_v4():
    return set(VisitRecordDC(**r) for r in users_visited_puket) - set(
        VisitRecordDC(**r) for r in users_visited_nz
    )