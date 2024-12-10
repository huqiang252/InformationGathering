#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/11/30
# 文件名称   ：类中的字典.py


class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


    def say(self):
        print(f"{self.name} {self.age} {self.sex}")


if __name__ == '__main__':
    p = Person("Tom", 18, "Male")
    print(p.__dict__)  #{'name': 'Tom', 'age': 18, 'sex': 'Male'}

    print(Person.__dict__)  #类返回的字典
    '''
    {
	'__module__': '__main__',
	'__init__': < function Person.__init__ at 0x0000023BBC5ECEE0 > ,
	'say': < function Person.say at 0x0000023BBC5ECD30 > ,
	'__dict__': < attribute '__dict__' of 'Person'objects > ,
	'__weakref__': < attribute '__weakref__' of 'Person' objects > ,
	'__doc__': None
}
    '''