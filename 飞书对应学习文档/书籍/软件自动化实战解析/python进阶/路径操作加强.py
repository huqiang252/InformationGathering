#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/25
from pathlib import Path

file_path = Path('/etc/ssh/ssh_host_key.pub')

print( file_path.name ) # 获取文件名 ssh_host_key.pub

print( file_path.suffix ) #后缀名 .pub

print( file_path.stem ) #ssh_host_key
