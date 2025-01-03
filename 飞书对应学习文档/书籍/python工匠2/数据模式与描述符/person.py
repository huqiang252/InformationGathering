#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/2
# 文件名称   ：person.py


class Person:
    """人
    :param name: 姓名
    :param age:年龄
    :param favorite_color:喜欢的颜色
    """
    def __init__(self, name, age,favorite_color):
        self.name = name
        self.age = age
        self.favorite_color = favorite_color

    def __str__(self):
        return self.name

    def __repr__(self):
        return '{cls_name}(name={name!r}, age={age!r}, favorite_color={color!r})'.format(
            cls_name=self.__class__.__name__,
            name=self.name,
            age=self.age,
            color=self.favorite_color,
        )

    def __format__(self, format_spec):
        """定义对象在字符串格式化时的行为
        :param format_spec: 需要的格式，默认为 ''
        """
        if format_spec == 'verbose':
            return f'{self.name}({self.age})[{self.favorite_color}]'
        elif format_spec == 'simple':
            return f'{self.name}({self.age})'
        return self.name





if __name__ == '__main__':
    p = Person('张三', 18, '红色')
    print(p) #张三
    print(p.__repr__()) #Person(name='张三', age=18, favorite_color='红色')
    print('{p:verbose}'.format(p=p))  #张三(18)[红色]
    print('{p:simple}'.format(p=p)) #张三(18)
    print(f'{p:verbose}') #张三(18)[红色]



