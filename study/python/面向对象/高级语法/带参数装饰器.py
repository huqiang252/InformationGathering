#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-07-27
# 接收装饰器参数的函数
# 参数一：以字符串形式接收被装饰函数的参数列表，需要与被装饰函数参数名保持一致，例："a,b,c"
# 参数二：以[(),(),()] 形式传入驱动数据。
def decorator_args(vars, datas):
    def decorator(func):
        # 将字符串参数分割备用
        v_keys = vars.split(",")
        # 定义保存 [{},{},{}] 形式的数据
        new_datas = []
        # 遍历数据，取出一组元素数据
        for item in datas:
            # 定义一个新字典，用来保存 变量名与传入数据组成的字典
            d_item = {}
            # 使用 zip 函数，同时遍历两个元组，变量名做为key, 元素数据做为value
            for k, v in zip(v_keys, item):
                # 将 变量名和值对应保存到字典中
                d_item[k] = v
            # 将组合好的字典追加到新数据中备用
            new_datas.append(d_item)
        def inner(*args, **kwargs):
            return func(*args, **kwargs)
        # 遍历新数据，取出元素字典
        for item in new_datas:
            # 将字典中的数据解包传给内函数
            inner(**item)
        return inner
    return decorator

# 数据驱动数据
data = [(1,2,3),(4,5,6),(7,8,9)]

# 装饰器传参
@decorator_args("a,b,c", data)
def show(a,b,c):
    print(a,b,c)
