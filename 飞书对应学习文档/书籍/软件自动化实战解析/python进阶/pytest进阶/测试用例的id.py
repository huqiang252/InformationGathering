#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/27

import pytest


def remove_whitespaces(input_str):
    # a buggy implementation
    return input_str.strip()


@pytest.mark.parametrize(
    "input_str, expected_str",
    [
        pytest.param("a bc", "abc", id="whitespace in the middle can be removed"),
        pytest.param("ab ", "ab", id="whitespace at the end can be removed"),
        pytest.param(" ab", "ab", id="在前面清除")
    ]
)
def test_remove_whitespaces(input_str, expected_str):
    actual = remove_whitespaces(input_str)
    assert actual == expected_str