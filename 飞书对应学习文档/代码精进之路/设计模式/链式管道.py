#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/14
# 文件名称   ：链式管道.py


from abc import ABC, abstractmethod

class Valve(ABC):
    @abstractmethod
    def process(self, data):
        raise NotImplementedError("子类必须实现 process 方法")

class UpperCaseValve(Valve):
    def process(self, data):
        return data.upper()

class ReverseValve(Valve):
    def process(self, data):
        return data[::-1]

class TailValve(Valve):
    def process(self, data):
        # 在这里可以执行一些最终的操作，比如日志记录
        print(f"TailValve - 最终数据: {data}")
        return data

class Pipeline:
    def __init__(self):
        self.valves = []
        self.tail_valve = None

    def add_valve(self, valve):
        self.valves.append(valve)

    def set_tail_valve(self, tail_valve):
        self.tail_valve = tail_valve

    def process(self, data):
        for valve in self.valves:
            data = valve.process(data)
        if self.tail_valve:
            data = self.tail_valve.process(data)
        return data

# 客户端
pipeline = Pipeline()
pipeline.add_valve(UpperCaseValve())
pipeline.add_valve(ReverseValve())

# 设置尾阀门
tail_valve = TailValve()
pipeline.set_tail_valve(tail_valve)

input_data = "hello world"
output_data = pipeline.process(input_data)
print(output_data)  # 输出: DLROW OLLEH

