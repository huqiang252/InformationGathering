#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/24
import re
import requests
from requests.exceptions import RequestException

def save_website_title(url, filename):
    # 抓取网页
    try:
        resp = requests.get(url)
    except RequestException as e:
        print(f'save failed: unable to get page content: {e}')
        return False
    # 获取标题
    obj = re.search(r'<title>(.*)</title>', resp.text)
    if not obj:
        print('save failed: title tag not found in page content')
        return False
    title = obj.group(1)
    # 保存文件
    try:
        with open(filename, 'w') as fp:
            fp.write(title)
    except IOError as e:
        print(f'save failed: unable to write to file {filename}: {e}')
        return False
    else:
        return True