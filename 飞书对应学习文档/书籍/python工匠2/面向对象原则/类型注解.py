#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/1
# 文件名称   ：类型注解.py

import random
from typing import List


class Duck:
    def __init__(self, color: str):
        self.color = color

    def quack(self) -> None:
        print(f"Hi, I'm a {self.color} duck!")


def create_random_ducks(number: int) -> List[Duck]:
    ducks: List[Duck] = []
    for _ in number:
        color = random.choice(['yellow', 'white', 'gray'])
        ducks.append(Duck(color=color))
    return ducks