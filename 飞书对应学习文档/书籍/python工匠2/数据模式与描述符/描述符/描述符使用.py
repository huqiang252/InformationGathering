#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/2
# 文件名称   ：描述符使用.py


class InfoDescriptor:
    """打印帮助信息的描述符"""
    def __get__(self, instance, owner=None):
        print(f'Calling __get__, instance: {instance}, owner: {owner}')
        if not instance:
            print('Calling without instance...')
            return self
        return 'informative descriptor'

    def __set__(self, instance, value):
        print(f'Calling __set__, instance: {instance}, value: {value}')

    def __delete__(self, instance):
        raise RuntimeError('Deletion not supported!')


class Foo:
    bar = InfoDescriptor()


if __name__ == '__main__':
    f = Foo()
    f.bar = 50  #Calling __set__, instance: <__main__.Foo object at 0x0000022D7CF2CFA0>, value: 50
    del f.bar  #RuntimeError: Deletion not supported!

