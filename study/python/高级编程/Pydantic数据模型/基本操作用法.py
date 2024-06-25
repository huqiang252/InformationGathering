#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-06-24
'''
Pydantic 是一个在 Python 中用于数据验证和解析的第三方库。它提供了一种简单且直观的方式来定义数据模型，并使用这些模型对数据进行验证和转换。

Pydantic 的一些主要特性：

类型注解：Pydantic 使用类型注解来定义模型的字段类型。你可以使用 Python 内置的类型、自定义类型或者其他 Pydantic 提供的验证类型。

数据验证：Pydantic 自动根据模型定义进行数据验证。它会检查字段的类型、长度、范围等，并自动报告验证错误。你可以使用 ValidationError 异常来捕获验证错误。

模型转换：Pydantic 提供了从各种数据格式（例如 JSON、字典）到模型实例的转换功能。它可以自动将输入数据解析成模型实例，并保留类型安全性和验证规则。


需要安装 pip install pydantic


'''


from pydantic import BaseModel, ValidationError
'''
使用 Pydantic，可以定义一个模型类，该类需要继承 pydantic 中的 BaseModel 类，模型类描述了数据的结构和类型，并指定验证规则。

然后，可以使用这个模型类来验证输入的数据是否符合预期，并以类型安全的方式访问和操作数据
如果创建实例的数据不符合类型注解的要求，则会报 ValidationError 错误。


'''

class User(BaseModel):
    name: str
    age: int
    email: str

try:
    user = User(name="Alice", age="30", email="alice@example.com")
except ValidationError as e:
    print(e.json())
