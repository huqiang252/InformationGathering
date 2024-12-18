#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/20


d = {'title':'foobar'}

d.setdefault('items',[]).append('foo')
print(d)  #{'title': 'foobar', 'items': ['foo']}

d.setdefault('items',[]).append('bar')
print(d) #{'title': 'foobar', 'items': ['foo', 'bar']}
