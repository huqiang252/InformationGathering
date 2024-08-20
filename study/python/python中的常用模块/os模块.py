#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-07-28
import os
directory = os.getcwd()
print("当前目录:", directory)

absolute_path = os.path.abspath('relative/path/to/file.txt')
print("Absolute Path:", absolute_path)


# 获取基本名称
base_name = os.path.basename('/path/to/file.txt')
print("Base Name:", base_name)



# 获取父目录路径
parent_directory = os.path.dirname('/path/to/file.txt')
print("父目录为:", parent_directory)

#os.path.split(path)：用于将一个路径拆分为目录部分和文件名部分。
path = '/home/user/file.txt'
result = os.path.split(path)
print(result)


#os.path.join(path)：用于连接多个路径部分。它将多个路径片段组合在一起，形成一个新的路径字符串。
path1 = '\home\user'
path2 = 'file.txt'
result = os.path.join(path1, path2)
print(result)



# 判断路径是否存在
path_to_check = '/path/to/file.txt'
if os.path.exists(path_to_check):
    print("路径存在")
else:
    print("路径不存在")