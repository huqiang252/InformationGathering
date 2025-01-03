#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/14
# 文件名称   ：结合使用.py


import pytest

# 定义阀门（Valve）
from abc import ABC, abstractmethod

class Valve(ABC):
    @abstractmethod
    def process(self, data):
        raise NotImplementedError("子类必须实现 process 方法")

class PreprocessValve(Valve):
    def process(self, data):
        print("PreprocessValve - 预处理数据")
        return [item.strip() for item in data]

class ConvertValve(Valve):
    def process(self, data):
        print("ConvertValve - 转换数据")
        return [item.upper() for item in data]

class ValidateValve(Valve):
    def process(self, data):
        print("ValidateValve - 验证数据")
        for item in data:
            assert len(item) > 0, f"数据项为空: {item}"
        return data

# 定义管道（Pipeline）
class Pipeline:
    def __init__(self):
        self.valves = []

    def add_valve(self, valve):
        self.valves.append(valve)

    def process(self, data):
        for valve in self.valves:
            data = valve.process(data)
        return data

# 定义 fixture 来设置管道
@pytest.fixture(scope="function")
def data_pipeline():
    pipeline = Pipeline()
    pipeline.add_valve(PreprocessValve())
    pipeline.add_valve(ConvertValve())
    pipeline.add_valve(ValidateValve())
    return pipeline

# 测试用例
def test_data_processing(data_pipeline):
    input_data = [" hello ", "world ", " stream ", " processing "]
    output_data = data_pipeline.process(input_data)
    expected_output = ["HELLO", "WORLD", "STREAM", "PROCESSING"]
    assert output_data == expected_output
    print("测试通过")
