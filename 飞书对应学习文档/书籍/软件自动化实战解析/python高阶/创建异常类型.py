#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-10-28

class NegativeScoreError(ValueError):
    pass

class CouponExpiredError(Exception):
    pass




if __name__ == '__main__':
    raise NegativeScoreError( '-5 is not a valid score' )
