#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/27


from datetime import datetime

def vip_only(func):
    def wrapper(*args, **kwargs):
        username = args[0]
        if username in ['Ava', 'Ema', 'Ryan']:
            func(*args, **kwargs)
            print(' - Executed at {}\r\n'.format(datetime.now()))
        else:
            print('Haha {}'.format(username))

    return wrapper
@vip_only
def greet(name):
    print('Hello {}!'.format(name))

greet('Ava')
greet('Ema')
greet('Li Ming')

# Hello Ava!
#  - Executed at 2024-10-27 22:59:09.738537
#
# Hello Ema!
#  - Executed at 2024-10-27 22:59:09.738537
#
# Haha Li Ming