#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-10-28


from datetime import datetime
import uuid


class QaRandom:
    TIMESTAMP_FORMAT = '%Y%m%d%H%M%S%f'

    @classmethod
    def timestamp(cls):
        return datetime.now().strftime( cls.TIMESTAMP_FORMAT )

    @classmethod
    def uuid(cls, name=''):
        if name:
            return uuid.uuid3( uuid.NAMESPACE_DNS, name )
        return uuid.uuid1()


if __name__ == '__main__':
    print( QaRandom.timestamp() )  # 20241028130913363922
    print( QaRandom.uuid() )
    print( QaRandom.uuid( '123456Abc' ) )
    print( QaRandom.uuid( '123456Abc' ) )
    print( QaRandom.uuid( '123456Abcd' ) )
