#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-06-24
from typing import Optional
from pydantic import BaseModel, EmailStr,ValidationError
#EmailStr 需要安装 pip install email-validator

class User(BaseModel):
    name: str
    age: int
    email: EmailStr
    phone: Optional[str] = None


# user = User(name="Alice", age=30, email="alice@example.com")  # 有效

try:
    user = User(name="Alice", age=30, email="invalid_email")  # 错误：无效的电子邮件
except ValidationError as e:
    print(e.json())