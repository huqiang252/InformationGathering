#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/2
# 文件名称   ：利用集合的游戏规则.py


class VisitRecord:
    """旅客记录
    :param first_name: 名
    :param last_name: 姓
    :param phone_number: 电话号码
    :param date_visited: 旅游时间
    """
    def __init__(self, first_name, last_name, phone_number, date_visited):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.date_visited = date_visited
    def __hash__(self):
        #自定义类的实例是可哈希的，但如果你重写了 __eq__ 方法，通常也需要重写 __hash__ 方法以保持一致性
        return hash(self.comparable_fields)
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.comparable_fields == other.comparable_fields
        return False
    @property
    def comparable_fields(self):
        """
        :return: 获取用于比较对象的字段值
        """
        return (self.first_name, self.last_name,self.phone_number)


def find_potential_customers_v2():
    #转换为VisitRecord对象计算集合差值
    return (set(VisitRecord(**r) for r in users_visited_pucket)
            - set(VisitRecord(**r) for r in users_visited_nz))


if __name__ == '__main__':
    #初始化，，两个属性一样的VisitRecord对象，会被认为不是同一个对象，因为没有重写__eq__方法
    v1 = VisitRecord('Alice', 'Smith', '123-456-7890', '2018-01-01')
    v2 = VisitRecord('Alice', 'Smith', '123-456-7890', '2018-01-01')

    #往集合加对象
    s = set()
    s.add(v1)
    s.add(v2)
    print(s) #{<__main__.VisitRecord object at 0x0000024D67D1DFD0>}


    print(v1==v2) #True