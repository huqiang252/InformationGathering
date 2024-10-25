#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-10-22

from datetime import datetime,timedelta
register_time=datetime.utcnow()  #2024-10-22 05:04:19.329702
print(register_time)

print(register_time+timedelta(days=7)) #2024-10-29 05:04:19.329702
