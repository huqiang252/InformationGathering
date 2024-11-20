#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/17


#以“千”为单位分隔数字
i = 1_1000_000
print(i+10)  #11000010


print(0.1+0.2)  #0.30000000000000004

from decimal import Decimal
#注意：这里的0.1,0.2必须是字符串
print(Decimal('0.1')+Decimal('0.2')) #0.3
print(Decimal(0.1)+Decimal(0.2))  #0.3000000000000000166533453694


numbers = [1,2,4,5,7]
print(sum(i%2==0  for i in numbers))  #2