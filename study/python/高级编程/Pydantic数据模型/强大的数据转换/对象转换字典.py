#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-06-24
'''

通过定义模型类，可以将通过网络传输或数据库查询的数据转换成模型类对象在程序中使用。

反之，也可以将处理过后的模型类对象转换成对应的字典或 JSON 数据进行存储或传输

'''

from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    name: str = Field(..., min_length=1, max_length=10)
    age: int = Field(..., ge=0, le=200)
    email: EmailStr
    phone: str = Field(default="13800138000", min_length=11, max_length=11)

user = User(name="Tom", age=22, email="alice@example.com")
# data = User.model_dump(user)
data = user.dict()
print(data)
print(type(data))
