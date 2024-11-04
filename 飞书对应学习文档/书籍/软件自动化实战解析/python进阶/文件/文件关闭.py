#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/26


#第一种写法
f=open('movies.txt',"r")
print( f.read() )
f.close()

print()
#第二种写法：为了避免这类问题，我们可以利用异常处理的功能，把文件关闭的逻辑放在finally代码块中
try:
    f = open( 'movies.txt', "r" )
    print( f.read() )
finally:
    f.close()

print()
#第三种写法,使用with：
with open('movies.txt','r') as f:
    print(f.read())