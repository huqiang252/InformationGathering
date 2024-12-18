#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/24


#创建或更新用户资料数据
# 如果是新用户，创建新Profile 数据，否则更新已有数据
if user.no_profile_exists:
    _update_or_create = create_user_profile
    extra_args = {'points': 0, 'created': now()}
else:
    _update_or_create = update_user_profile
    extra_args = {'updated': now()}

_update_or_create(
    username=user.username,
    gender=user.gender,
    email=user.email,
    age=user.age,
    address=user.address,
    **extra_args,
)