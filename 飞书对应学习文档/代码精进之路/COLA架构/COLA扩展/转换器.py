#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/17
# 文件名称   ：转换器.py


from marshmallow import Schema, fields

class User:
    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email

class UserSchema(Schema):
    user_id = fields.Int(required=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)

# 转换函数
def user_to_user_dto(user: User, schema: Schema) -> dict:
    return schema.dump(user)

def user_dto_to_user(user_dto: dict, schema: Schema) -> User:
    data = schema.load(user_dto)
    return User(**data)




if __name__ == "__main__":
    user_schema = UserSchema()
    user = User(user_id=1, username='john_doe', email='john@example.com')
    user_dto = user_to_user_dto(user, user_schema)
    print("User to UserDTO:", user_dto)

    user_from_dto = user_dto_to_user(user_dto, user_schema)
    print("UserDTO to User:", user_from_dto)
