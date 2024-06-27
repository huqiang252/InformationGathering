#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-06-25
from pydantic import BaseModel, EmailStr, validator
from typing import Optional

class User(BaseModel):
    name: str
    age: int
    email: EmailStr
    phone: Optional[str] = None

    @validator('age')
    def check_age(cls, age):
        if age < 18:
            raise ValueError("用户年龄必须大于18岁")
        return age


user = User(name="Alice", age=18, email="alice@example.com")  # 错误：用户年龄必须大于18岁
