#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/23
from collections import deque

def deque_append():
    l = deque()
    for i in range(5000):
        l.append(i)


def deque_appendleft():
    l = deque()
    for i in range(5000):
        l.appendleft(i)

import timeit
# 默认执行 1 万次
append_spent = timeit.timeit(
    setup='from __main__ import deque_append',
    stmt='deque_append()',
    number=10000,
)
print("deque_append:", append_spent)
insert_spent = timeit.timeit(
    setup='from __main__ import deque_appendleft',
    stmt='deque_appendleft()',
    number=10000,
)
print("deque_appendleft", insert_spent)