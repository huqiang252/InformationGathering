#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/26

class Range7:
    """
    生成某个范围内可被7整除或包含7的整数
    """
    def __init__(self, start, stop):
        '''
        :param start: 开始数字
        :param stop: 结束数字
        '''
        self.start = start
        self.stop = stop
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            # 如果当前数字到达边界就抛出异常
            if self.current >= self.stop:
                raise StopIteration
            # 如果满足要求就返回数据
            if self.num_is_valid( self.current ):
                ret = self.current
                self.current += 1
                return ret
            # 不返回继续下一个迭代
            self.current += 1

    #判断数字是否满足要求""
    def num_is_valid(self,num):
        #是否包含7或能被7整除
        if num ==0:
            return False
        return num%7==0 or "7" in str(num)


if __name__ == '__main__':
    r = Range7(0,20)
    print(tuple(r)) #(7, 14, 17)
    print(tuple(r))  #()   二次遍历就会拿不到结果