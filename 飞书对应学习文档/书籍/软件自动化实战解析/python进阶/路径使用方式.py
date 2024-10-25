#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/25

from pathlib import Path


print(Path.home()) #Home路径
print(Path.cwd()) #当前路径
print(Path.cwd().parent) #当前路径上一级路径
print(Path.cwd().parent.parent) #当前路径上2级路径

path  = Path('D:/InformationGathering/飞书对应学习文档') #用字符串构造path对象
print(path.joinpath("exampls","1")) #D:\InformationGathering\飞书对应学习文档\exampls\1
print(path.joinpath("exampls","1").joinpath("kkwal")) #D:\InformationGathering\飞书对应学习文档\exampls\1\kkwal

print(path.joinpath("学习乐园").exists())  #判断路径是否存在  True

#根据路径删除文件
my_file_path = Path('/etc/data0/opt/tomcat/logs')

# my_file_path.unlink() #如果指定的文件路径并不存在，那unlink方法会抛出FileNotFoundError

my_file_path.unlink(missing_ok=True)  #提供额外的参数给unlink方法，让它忽略文件不存在的情况，不要抛出异常

#创建文件
my_path = Path('D:/InformationGathering/飞书对应学习文档/学习乐园/人工智能')
my_path.mkdir(parents=True,exist_ok=True) #parents创建多级目录;exist_ok判断路径是否存在

print()
#判断路径是文件夹 还是文件
new_path = Path('D:\InformationGathering\飞书对应学习文档\书籍\软件自动化实战解析\python进阶')
print(new_path.is_dir()) #True  判断是否为文件夹
print(new_path.is_file()) #False 判断是否为文件
print(new_path.joinpath("utc时间.py").is_file()) #True