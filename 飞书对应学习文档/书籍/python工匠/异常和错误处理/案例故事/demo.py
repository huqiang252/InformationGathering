#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/24
import re
text="""
<html>
<head>
<title>Hello World</title>
</head>
<body>
<h1>Hello World</h1>
</body>
</html>
"""
obj = re.search(r'<title>(.*)</title>', text)
obj.grop(1)