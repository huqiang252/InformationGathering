#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/29
import pytest
from QaParameterSet import QaParameterSet


def remove_whitespaces(input_str):
    return input_str.strip()

@pytest.mark.parametrize("test_definition", [
        QaParameterSet.param({"input": " \t ab", "expected": "ab"}, id="Adjacent whitespaces can be removed as expected"),
        QaParameterSet.param({"input": " ab \t c", "expected": "abc"}, id="Separated whitespaces can be removed as expected"),
        QaParameterSet.param({"input": "ab ", "expected": "ab"}, id="尾部的空白字符可以被正确删除"),

    ]
)
def test_remove_whitespaces(test_definition):
    actual = remove_whitespaces(test_definition['input'])
    assert actual == test_definition['expected']