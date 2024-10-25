#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-10-22

#
# from datetime import datetime
# local_time = datetime.now()
# utc_time = datetime.utcnow()
# print(local_time)#2024-10-22 17:07:41.393182
# print(utc_time) #2024-10-22 09:07:41.393182



from datetime import datetime, timezone

TIME_FORMAT = "%Y_%m_%d, %H:%M"
local_time = datetime.now()
print('local time:', local_time.strftime(TIME_FORMAT))  #2024_10_22, 17:36

utc_time = datetime.now(timezone.utc)
print("utc time:", utc_time.strftime(TIME_FORMAT)) #utc time: 2024_10_22, 09:36

print('local time converted from utc:', utc_time.astimezone().strftime(TIME_FORMAT))