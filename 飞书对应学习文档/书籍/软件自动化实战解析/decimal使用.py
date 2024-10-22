#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-10-21


from decimal import Decimal
from decimal import getcontext
r=Decimal('3.14')+ Decimal('1.21')
print(r)  #4.35
print( getcontext() )  #Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])
getcontext().prec=30

r1 = Decimal('11.231211')+ Decimal('22.92322')
print(r1) #34.154431
print( getcontext() )

annual_income = Decimal('100000')
print(annual_income)
getcontext().prec = 30 #有副作用，导致小数点很多位
r=annual_income / 12
print(r) #8333.33333333333333333333333333
print( round( r, 2 ) ) #8333.33  配合使用round方法，可以得到我们期望的精确度





