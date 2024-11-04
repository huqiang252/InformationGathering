
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/27


import pytest

def remove_whitespaces(input_str):
    # a buggy implementation
    return input_str.strip()

test_data = [
    ("a bc", "abc"),
    ("ab ", "ab"),
    (" ab", "ab"),
    (" \t ab", "ab"),
    (" ab \t c", "abc"),
    ("  \t \t\t ", ""),
    ("", ""),
    (None, None)
]

@pytest.mark.parametrize("input_str, expected_str", test_data)
def test_remove_whitespaces(input_str, expected_str):
    actual = remove_whitespaces(input_str)
    assert actual == expected_str