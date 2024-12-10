#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/11/30
# 文件名称   ：filepath.py



import os
class FilePath:
    def __init__(self,path):
        self.path = path
    @property
    def basename(self):
        return os.path.basename(self.path)

    @basename.setter
    def basename(self, name):
        """修改当前路径里的文件名部分"""
        self.path = os.path.join(os.path.dirname(self.path), name)

    @basename.deleter
    def basename(self):
        raise RuntimeError('Can not delete basename!')




if __name__ == '__main__':
    fp = FilePath('E:\InformationGathering\飞书对应学习文档\书籍\python工匠2\面向对象编程')
    fp.basename='bar.txt'
    print(fp.path) #E:\InformationGathering\飞书对应学习文档\书籍\python工匠2\bar.txt
    del fp.basename  #RuntimeError: Can not delete basename!


