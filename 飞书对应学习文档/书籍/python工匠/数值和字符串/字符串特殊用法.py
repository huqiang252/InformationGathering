#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/17


def extract_value(s):
    items = s.split(':')
    # 因为 s 不一定会包含 ':'，所以需要对结果长度进行判断
    if len(items) == 2:
        return items[1]
    else:
        return ''

def extract_value_v2(s):
    # 当 s 包含分隔符 : 时，元组最后一个成员刚好是value
    # 若是没有分隔符，最后一个成员默认是空字符串 ''
    return s.partition(':')[-1]



if __name__ == '__main__':
    print( extract_value( 'name:piglei' ) )  #piglei
    print( extract_value( 'age' ) ) #空字符

    print( extract_value_v2( 'name:piglei' ) ) #piglei
    print( extract_value_v2( 'age' ) )
