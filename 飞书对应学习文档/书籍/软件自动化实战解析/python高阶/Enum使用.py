#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-10-28
from enum import Enum

class EncodingEnum(Enum):
    UTF8 = "utf-8"
    UTF16 = 'utf-16'
    ASCII = 'ascii'

def set_encoding(char_encoding_enum):
    print(char_encoding_enum)
    print(char_encoding_enum.value)

set_encoding(EncodingEnum.UTF8)


