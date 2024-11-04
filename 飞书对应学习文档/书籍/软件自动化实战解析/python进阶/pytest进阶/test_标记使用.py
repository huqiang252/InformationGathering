#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/27

import pytest

class TestBrowsers:

    @pytest.mark.P0
    @pytest.mark.UI
    @pytest.mark.Regression
    def test_chrome(self):
        ...

    @pytest.mark.P1
    @pytest.mark.UI
    def test_safari(self):
        ...

    @pytest.mark.P1
    def test_firefox(self):
        ...

    @pytest.mark.P2
    def test_edge(self):
        ...


