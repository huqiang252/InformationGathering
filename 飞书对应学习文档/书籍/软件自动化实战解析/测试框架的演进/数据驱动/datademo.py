#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/29
import pytest
from QaParameterSet import QaParameterSet
def remove_whitespaces(input_str):
    # a buggy implementation
    return input_str.strip()

@pytest.mark.parametrize(
    "input_str, expected_str",
    [
        QaParameterSet.param("a bc", "abc", id="whitespace in the middle can be removed"),
        QaParameterSet.param("ab ", "abd", id="尾部的空白字符可以被正确删除")
    ]
)
def test_remove_whitespaces(input_str, expected_str):
    actual = remove_whitespaces(input_str)
    assert actual == expected_str