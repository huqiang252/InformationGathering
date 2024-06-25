#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-06-25
'''

Pydantic在API开发中的应用非常广泛，特别是在需要严格数据验证和序列化的场景。
例如，开发一个RESTful API时，
可以使用Pydantic来定义请求体和响应体的数据结构。以下是一个使用Pydantic进行API开发的示例

'''

from pydantic import BaseModel
from typing import List


class User(BaseModel):
    id: int
    name: str
    email: str

class UserList(BaseModel):
    users: List[User]

def get_users() -> UserList:
    # 模拟从数据库获取用户数据
    users_data = [
        {"id": 1, "name": "Alice", "email": "alice@example.com"},
        {"id": 2, "name": "Bob", "email": "bob@example.com"}
    ]
    return UserList(users=users_data)


if __name__ == '__main__':
    print(get_users())