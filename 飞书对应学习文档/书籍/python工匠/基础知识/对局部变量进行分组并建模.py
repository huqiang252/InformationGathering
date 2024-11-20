#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/16


class ImportedSummary:
    """保存导入结果摘要的数据类"""

    def __init__(self):
        self.succeeded_count = 0
        self.failed_count = 0

class ImportingUserGroup:
    """用于暂存用户导入处理的数据类"""

    def __init__(self):
        self.duplicated = []
        self.banned = []
        self.normal = []

def import_users_from_file(fp):
    """尝试从文件对象读取用户，然后导入数据库　　

    :param fp: 可读文件对象
    :return: 成功与失败的数量
    """
    importing_user_group = ImportingUserGroup()
    for line in fp:
        parsed_user = parse_user(line)
        # …… 进行判断处理，修改上面定义的importing_user_group 变量

    summary = ImportedSummary()
    # …… 读取 importing_user_group，写入数据库并修改成功与失败的数量

    return summary.succeeded_count, summary.failed_count