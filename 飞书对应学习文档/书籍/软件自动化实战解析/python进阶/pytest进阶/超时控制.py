#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/27
import pytest
import time

class TestBrowsers:
    @pytest.mark.timeout(8)
    def test_safari(self):
        time.sleep(10)