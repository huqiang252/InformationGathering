#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/24


#同步用户资料到外部系统，仅当同步成功时发送通知消息
try:
    sync_profile(user.profile, to_external=True)
except Exception as e:
    print("Error while syncing user profile")
else:
    send_notification(user, 'profile sync succeeded')