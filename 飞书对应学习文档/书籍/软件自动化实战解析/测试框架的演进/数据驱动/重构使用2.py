#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/29
import pytest
from QaParameterSet import QaParameterSet


def remove_whitespaces(input_str):
    return input_str.strip()

@pytest.mark.parametrize("test_definition", [
        QaParameterSet.dict_param({"description": "Adjacent whitespaces can be removed as expected", "input": " \t ab", "expected": "ab"}),
        QaParameterSet.dict_param({"description": "Separated whitespaces can be removed as expected", "input": " ab \t c", "expected": "abc"})
    ]
)
def test_remove_whitespaces(test_definition):
    actual = remove_whitespaces(test_definition['input'])
    assert actual == test_definition['expected']