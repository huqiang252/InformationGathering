#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/29


from enum import Enum
class TrainTypeEnum(Enum):
    GaoTie = 'G'    # GC-高铁/城际
    DongChe = 'D'   # D-动车
    ZhiDa = 'Z'     # Z-直达
    TeKuai = 'T'    # T-特快
    KuaiSu = 'K'    # K-快速
    QiTa = 'QT'     # 其他



