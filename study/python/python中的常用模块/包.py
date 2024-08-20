#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-07-28


'''
__init__.py 文件是包的初始化文件，该文件是是区别包与文件夹的关键。

当使用 from-import 方式导入时，可以通过在文件中添加魔法属性 __all__ 属性来设置包中哪些模块可以被导入。
'''

# 在 __init__.py 中添加下面代码
__all__ = ["mm"]

# main.py中的代码
from mp import *
# 此时只能使用 __all__ 中指定的mm模块，nn 模块不能使用
mm.show()
