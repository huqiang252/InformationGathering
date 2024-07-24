#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-07-24
name = "Alice"
age = 30
greeting = f"{'Hello' if age < 30 else 'Hi'} {name.upper()}"
print(greeting)
# 输出：Hello Alice


# 字符串对齐
print(f"The value is ljust: |{'abc':5}|")
print(f"The value is ljust: |{'abc':<5}|")
print(f"The value is rjust: |{'abc':>5}|")
# 数字对齐
print(f"The value is rjust: |{11:5}|")
print(f"The value is rjust: |{11:>5}|")
print(f"The value is ljust: |{11:<5}|")
# 小数保留
print(f"The value is rjust: |{3.1415926:5.2f}|")
