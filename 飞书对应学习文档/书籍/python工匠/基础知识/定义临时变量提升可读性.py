#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/16
user= None

#为所有性别为女或者级别大于3的活跃用户发放10000个金币
user_is_eligible = user.is_active and (user.sex == 'female' or user.level > 3)



if user_is_eligible:
    user.add_coins(10000)



