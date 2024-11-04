#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/27


import pytest
import random

@pytest.fixture()
def random_int():
    return random.randrange(1000)


def test_remove_whitespaces(random_int):
    print('random integer:', random_int)
    assert random_int < 500, 'random integer should be less than 500'



if __name__ == '__main__':
    pytest.main(['-s','-v'])