#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-06-24
from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    name: str = Field(..., min_length=1, max_length=10)
    age: int = Field(..., ge=0, le=200)
    email: EmailStr
    phone: str = Field(default="13800138000", min_length=11, max_length=11)

user = User(name="Tom", age=22, email="alice@example.com")
data = User.model_dump_json(user)
print(data)
print(type(data))
