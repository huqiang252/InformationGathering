#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-10-20
import os
from config_all import setting

from mitmproxy.tools.main import mitmdump,mitmweb


#设置延迟2秒
# mitmdump --set delay=2

#启用带宽限制 模拟秒100kb的带宽限制速度
#mitmdump --set bandwidth=100

# mitmdump(['-s', 'mitmTcpDemo.py'])
# mitmdump(['-s', setting.mitmproxy_path,'--ssl-insecure'])  #主站
mitmdump(['-s', setting.mitmproxy_newpath,'--ssl-insecure'])  #主站


# os.system(
#             f'mitmdump -p 9922  -s  {setting.mitmproxy_path}  --ssl-insecure  --set block_global=false')  #-q 是静默不打印日志
