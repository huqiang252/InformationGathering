#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-06-26
import json

class InnerClass:
    def __init__(self, inner_attr):
        self.inner_attr = inner_attr

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        return cls(**json.loads(json_str))

class OuterClass:
    def __init__(self, outer_attr, inner_instance):
        self.outer_attr = outer_attr
        self.inner_instance = inner_instance

    def to_json(self):
        # 首先序列化内部实例
        inner_json = self.inner_instance.to_json()
        # 然后序列化外部实例，包括内部实例的json表示
        return json.dumps({
            'outer_attr': self.outer_attr,
            'inner_instance': inner_json
        })

    @classmethod
    def from_json(cls, json_str):
        # 首先反序列化外部实例
        data = json.loads(json_str)
        # 然后反序列化内部实例
        inner_instance = InnerClass.from_json(data['inner_instance'])
        # 使用反序列化得到的内部实例创建外部实例
        return cls(data['outer_attr'], inner_instance)

# 创建内部类的实例
inner_obj = InnerClass('inner_value')

# 创建外部类的实例，包含内部类实例
outer_obj = OuterClass('outer_value', inner_obj)

# 将外部实例序列化为json字符串
outer_json = outer_obj.to_json()
print(outer_json)  # 输出: {"outer_attr": "outer_value", "inner_instance": {"inner_attr": "inner_value"}}

# 将json字符串反序列化为外部类实例
new_outer_obj = OuterClass.from_json(outer_json)
print(new_outer_obj.outer_attr)  # 输出: outer_value
print(new_outer_obj.inner_instance.inner_attr)  # 输出: inner_value