#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-10-20
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
print(BASE_DIR)
sys.path.append(BASE_DIR)

#mitmmproxy 运行路径
mitmproxy_path=os.path.join( BASE_DIR, 'mitmproxyRun', 'mitmdumpHelp.py' )
print(mitmproxy_path)