#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/2
# 文件名称   ：fooDel.py


class Foo:

    def __del__(self):
        print(f'cleaning up {self}...')



if __name__ == '__main__':
    foo = Foo()
    h = {'com': foo}
    l = [foo, ]
    del foo #不会立即删除
    print(h)
    print(l)
    print(foo)


#{'com': <__main__.Foo object at 0x000001FEDA48CFD0>}
# [<__main__.Foo object at 0x000001FEDA48CFD0>]
# cleaning up <__main__.Foo object at 0x000001FEDA48CFD0>...