#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/29

def test_error_collector():

    assert 1 + 2 == 4, "error 1"
    assert 6 - 2 == 2, "error 2"
    assert 2 * 2 == 8, "error 3"
    assert 6 / 2 == 2, "error 4"



#改进后
def test_error_collector2():
    error_messages = ""
    if 1 + 2 != 4:
        error_messages = '\nerror 1'

    if 6 - 2 != 2:
        error_messages += '\nerror 2'

    if 2 * 2 != 8:
        error_messages += '\nerror 3'

    if 6 / 2 != 2:
        error_messages += '\nerror 4'

    assert not error_messages, 'Validation failed because:' + error_messages

