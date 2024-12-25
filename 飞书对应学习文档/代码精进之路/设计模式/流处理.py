#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/14
# 文件名称   ：流处理.py
from abc import ABC, abstractmethod


#定义阀门
class Valve(ABC):
    @abstractmethod
    def process(self, data):
        raise NotImplementedError("子类必须实现 process 方法")


class UpperCaseValve(Valve):
    def process(self, data):
        for item in data:
            yield item.upper()

class ReverseValve(Valve):
    def process(self, data):
        for item in data:
            yield item[::-1]


#定义管道
class Pipeline:
    def __init__(self):
        self.valves = []

    def add_valve(self, valve):
        self.valves.append(valve)

    def process(self, data):
        for valve in self.valves:
            data = valve.process(data)
        return data



if __name__ == "__main__":
    # 创建阀门
    upper_case_valve = UpperCaseValve()
    reverse_valve = ReverseValve()

    # 创建管道并添加阀门
    pipeline = Pipeline()
    pipeline.add_valve(upper_case_valve)
    pipeline.add_valve(reverse_valve)

    # 创建数据流
    input_data = ["hello", "world", "stream", "processing"]

    # 处理数据流
    output_data = pipeline.process(input_data)

    # 打印输出数据
    for item in output_data:
        print(item)
