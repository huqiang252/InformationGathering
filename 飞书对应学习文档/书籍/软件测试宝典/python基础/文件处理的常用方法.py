#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-10-18


#创建一个写文件，覆盖写
f = open('1.txt','w')
f.write('fffff\n')
f.close()
print('-'*50)


##追加写入多行
f1 = open('2.txt','a')
f1.writelines(['1\n','2\n'])
f1.close()
print('_'*50)

##
f3 = open('1.txt','r')
print(f3.readlines())  #['fffff\n']
f3.close()