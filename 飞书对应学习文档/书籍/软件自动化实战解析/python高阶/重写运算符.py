#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/27


class CustomerOrder:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return CustomerOrder(self.amount + other.amount)


if __name__ == '__main__':
    order1 = CustomerOrder( 100 )
    order2 = CustomerOrder( 2000 )

    order_added = order1 + order2
    print(order_added.amount) #2100