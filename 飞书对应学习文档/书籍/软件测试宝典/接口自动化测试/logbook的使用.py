#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-10-19

import os
import logbook
from logbook import Logger,TimedRotatingFileHandler
from logbook.more import ColorizedStderrHandler

def log_type(record,handler):
    log = "[{date}][{level}][{filename}][{func_name}][{lineno}]{msg}".format(
        date=record.time, #日志时间
        level=record.level_name, #日志等级
        filename = os.path.split(record.filename)[-1], #文件名
        func_name = record.func_name,#函数名
        lineno = record.lineno, #行号
        msg = record.message #日志内容
    )

    return log

#日志存储路径
LOG_DIR = os.path.join('Log')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)


#日志打印到屏幕
log_std = ColorizedStderrHandler(bubble=True)
log_std.formatter = log_type


#日志打印到文件
log_file = TimedRotatingFileHandler(
    os.path.join(LOG_DIR,'%s.log'%'log'),
    date_format='%Y-%m-%d',
    bubble=True,
    encoding='utf-8'
)

log_file.formatter = log_type


#脚本日志
log = Logger('script')
def init_logger():
    logbook.set_datetime_format("local")
    log.handlers=[]
    log.handlers.append(log_file)
    log.handlers.append(log_std)


#实例化，默认调用
logger = init_logger()


if __name__ == '__main__':
    log.info('测试')