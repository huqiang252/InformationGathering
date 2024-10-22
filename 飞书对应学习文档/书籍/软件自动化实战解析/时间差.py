#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-10-22
from datetime import datetime
start_time=datetime(2024,10,22,11,8,44,61186)

end_time=datetime.now()
print(end_time)  #2024-10-22 11:08:16.216342

time_elapsed= end_time-start_time
print(time_elapsed.total_seconds())