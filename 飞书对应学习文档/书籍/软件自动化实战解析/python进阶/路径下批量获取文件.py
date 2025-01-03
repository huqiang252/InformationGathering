#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/25
from pathlib import Path

for f in Path.cwd().glob('*'):   #glob函数只针对指定的文件夹，不会递归遍历到子文件夹中
    print(f.name)

print()

for f in Path.cwd().rglob('*'):  #如果想进行递归遍历操作，需要用rglob方法，这里的r代表recursive
    print(f.name)

print()

for f in Path.cwd().glob('自定义排序*.py'): #根据通配符过滤文件
    print(f.name)


#获取文件大小
new_path = Path('D:\InformationGathering\飞书对应学习文档\书籍\软件自动化实战解析\python进阶')
print(new_path.stat().st_size) #4096（字节单位）