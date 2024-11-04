#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/26


# mod.py
def is_even_nuber(val):
    val = int(val)
    if val % 2 == 0:
        return True
    return False

def loop_inputs():
    user_input = input('Please input an integer: ')
    while user_input != 'exit':
        if is_even_nuber(user_input):
            print(user_input, 'is even number')
        else:
            print(user_input, 'is NOT even number')
        user_input = input('Please input an integer: ')

if __name__ == '__main__':
    loop_inputs()
else:
    print('__name__ =', __name__)