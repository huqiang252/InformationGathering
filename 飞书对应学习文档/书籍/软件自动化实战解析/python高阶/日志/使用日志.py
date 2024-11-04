#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-10-28
import logging
mylog = logging.getLogger(__name__)

#我们指定Handler时的方法名叫作“addHandler”，而不是“setHandler”，
# 这意味着我们可以指定多个Handler，可以做到让日志同时输出到Console和物理文件中。
fileHandle= logging.FileHandler('my.log')
mylog.addHandler(fileHandle)


stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.WARNING)

stream_formatter = logging.Formatter('%(module)s, %(asctime)s, %(levelname)s:%(message)s')
stream_handler.setFormatter(stream_formatter)
mylog.addHandler(stream_handler)





if __name__ == '__main__':

    mylog.warning("slfj")
    mylog.error("adfkahfdl")


    try:
        with open( 'file_not_exists.log' ) as f:
            lines = f.readlines()
            print( lines )
    except Exception as err: #error方法支持一个参数exc_info，当我们把这个参数指定为true时，可以得到完整的异常信息栈
        mylog.error( err, exc_info=True )