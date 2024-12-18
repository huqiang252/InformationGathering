#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/26


class Range7:
    """生成某个范围内可被 7 整除或包含 7 的数字"""
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __iter__(self):
        # 返回一个新的迭代器对象
        return Range7Iterator(self)  #相当于每次一个新对象

class Range7Iterator:
    def __init__(self, range_obj):
        self.range_obj = range_obj #组装
        self.current = range_obj.start
    def __iter__(self):
        return self
    def __next__(self):
        while True:
            if self.current >= self.range_obj.end:
                raise StopIteration
            if self.num_is_valid(self.current):
                ret = self.current
                self.current += 1
                return ret
            self.current += 1
    def num_is_valid(self, num):
        if num == 0:
            return False
        return num % 7 == 0 or '7' in str(num)

if __name__ == '__main__':
    r = Range7(0,20)
    print(tuple(r)) #(7, 14, 17)
    print(tuple(r)) ##(7, 14, 17)