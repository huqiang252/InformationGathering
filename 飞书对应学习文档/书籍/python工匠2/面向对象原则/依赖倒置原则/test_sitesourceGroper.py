#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/2
# 文件名称   ：test_sitesourceGroper.py


from collections import Counter

def test_grouper_from_local():
    page = LocalHNWebPage(path="./static_hn.html")
    grouper = SiteSourceGrouper(page)
    result = grouper.get_groups()
    assert isinstance(result, Counter), "groups should be Counter instance"


