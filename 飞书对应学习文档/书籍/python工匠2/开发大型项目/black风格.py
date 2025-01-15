#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2025/1/12
# 文件名称   ：black风格.py


#1.代码稍微长了一点儿，black会尝试将所有参数单独换行
User.objects.create(
    name="piglei", gender="M", language="Python", status="active", points=100
)

# 2. 代码过长，black 会让每个参数各占一行
User.objects.create(
    name="piglei",
    gender="M",
    language="Python",
    status="active",
    points=100,
    location="Shenzhen",
)