#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-06-25
from pydantic import BaseModel, Field, EmailStr
class User(BaseModel):
    name: str
    age: int
    email: str

json_data = '{"name":"Tom","age":22,"email":"alice@example.com","phone":"13800138000"}'
user = User.parse_raw(json_data)
print(user)
print(type(user))