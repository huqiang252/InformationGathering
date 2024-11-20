#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/19
class User:
    def __init__(self, name, active):
        self.name = name
        self.is_active = active

from textwrap import dedent
#dedent方法会删除整段字符串左侧的空白缩进。使用它来处理多行字符串以后，整段代码的缩进视觉效果就能保持正常了
def main2():
    user = User('Alice', True)
    if user.is_active:
        message = dedent("""\
            Welcome, today's movie list:
            - Jaw (1975)
            - The Shining (1980)
            - Saw (2004)""")
        print(message)



if __name__ == '__main__':
    # main()
    main2()


