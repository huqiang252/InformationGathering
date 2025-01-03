#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/26


def process_tasks(tasks):
    """批量处理任务，如果遇到状态不为 pending 的任务，则中止本次处理"""
    non_pending_found = False
    for task in tasks:
        if not task.is_pending():
            non_pending_found = True
            break
        process(task)

    if non_pending_found:
        notify_admin('Found non-pending task, processing aborted.')
    else:
        notify_admin('All tasks was processed.')



#使用for else 结构
def process_tasks(tasks):
    """批量处理任务，如果遇到状态不为 pending 的任务，则中止本次处理"""
    for task in tasks:
        if not task.is_pending():
            notify_admin('Found non-pending task, processing aborted.')
            break
        process(task)
    else:
        notify_admin('All tasks was processed.')


def process_tasks(tasks):
    """批量处理任务并将结果通知管理员"""
    if _process_tasks(tasks):
        notify_admin('All tasks was processed.')
    else:
        notify_admin('Found non-pending task, processing aborted.')


def _process_tasks(tasks):
    """批量处理任务，如果遇到状态不为 pending 的任务，则中止本次处理

    :return: 是否完全处理所有任务
    :rtype: bool
    """
    for task in tasks:
        if not task.is_pending():
            return False
        process(task)
    return True