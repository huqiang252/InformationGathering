#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/1
# 文件名称   ：appConfig.py


class AppConfig:
    """程序配置类，使用单例模式"""
    def __init__(self): ➊
        # 省略：从外部配置文件读取配置
        ...
_config = AppConfig() ➋


