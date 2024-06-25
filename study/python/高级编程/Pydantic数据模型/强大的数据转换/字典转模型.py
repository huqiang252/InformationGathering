#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-06-24
from pydantic import BaseModel, Field, EmailStr
class User(BaseModel):
    name: str
    age: int
    email: str

dict_data = {'name': 'Tom', 'age': 22, 'email': 'alice@example.com'}
user = User.model_validate(dict_data)
print(user)
print(type(user))