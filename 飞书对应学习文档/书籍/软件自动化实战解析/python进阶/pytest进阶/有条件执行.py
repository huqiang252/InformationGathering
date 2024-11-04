#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/27

import platform
import pytest

def is_mac_catalina():
    if platform.system() != 'Darwin':
        return False

    mac_version = platform.mac_ver()[0]  # something like '10.14.6'
    version_parts = mac_version.split('.')
    if version_parts[0] == '10' and version_parts[1] == '14':
        return True

    return False

mac_catalina_only = pytest.mark.skipif(not is_mac_catalina, reason='Safari testing against Mac OS only')

class TestBrowsers:

    def test_chrome(self):
        pass

    def test_edge(self):
        pass

    @mac_catalina_only
    def test_safari(self):
        pass