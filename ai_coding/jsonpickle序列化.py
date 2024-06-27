#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-06-26

import jsonpickle

class InnerClass:
    def __init__(self, inner_attr):
        self.inner_attr = inner_attr

class OuterClass:
    def __init__(self, outer_attr, inner_instance):
        self.outer_attr = outer_attr
        self.inner_instance = inner_instance

# 创建内部类的实例
inner_obj = InnerClass('inner_value')

# 创建外部类的实例，包含内部类实例
outer_obj = OuterClass('outer_value', inner_obj)

# 将外部实例序列化为json字符串
outer_json = jsonpickle.encode(outer_obj)
print(outer_json)  # 输出: {"py/object": "__main__.OuterClass", "outer_attr": "outer_value", "inner_instance": {"py/object": "__main__.InnerClass", "inner_attr": "inner_value"}}

# 将json字符串反序列化为外部类实例
new_outer_obj = jsonpickle.decode(outer_json)
print(new_outer_obj.outer_attr)  # 输出: outer_value
print(new_outer_obj.inner_instance.inner_attr)  # 输出: inner_value