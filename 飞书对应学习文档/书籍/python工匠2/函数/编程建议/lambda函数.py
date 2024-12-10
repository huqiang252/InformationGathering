#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/11/30
# 文件名称   ：lambda函数.PY
data=[{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 20}]
#方式1
print(sorted(data, key=lambda obj: obj['name']))

#方式2
from operator import itemgetter
print(sorted(data, key=itemgetter('age')))
#[{'name': 'Charlie', 'age': 20}, {'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]