#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/7


class Customer:
    """客户"""

    def __init__(self, name):
        self.__name = name
        self.__num = 0
        self.__clinics = None

    def getName(self):
        return self.__name

    def register(self, system):
        system.pushCustomer(self)

    def setNum(self, num):
        self.__num = num

    def getNum(self):
        return self.__num

    def setClinic(self, clinic):
        self.__clinics = clinic

    def getClinic(self):
        return self.__clinics


class NumeralIterator:
    """迭代器"""

    def __init__(self, data):
        self.__data = data
        self.__curIdx = -1

    def next(self):
        """移动至下一个元素"""
        if (self.__curIdx < len(self.__data) - 1):
            self.__curIdx += 1
            return True
        else:
            return False

    def current(self):
        """获取当前的元素"""
        return self.__data[self.__curIdx] if (self.__curIdx < len(self.__data) and self.__curIdx >= 0) else None


class NumeralSystem:
    """排号系统"""

    __clinics = ("1号分诊室", "2号分诊室", "3号分诊室")

    def __init__(self, name):
        self.__customers = []
        self.__curNum = 0
        self.__name = name

    def pushCustomer(self, customer):
        customer.setNum(self.__curNum + 1)
        print(f'{self.__curNum}%{len(NumeralSystem.__clinics)}={self.__curNum % len(NumeralSystem.__clinics)}')
        click = NumeralSystem.__clinics[self.__curNum % len(NumeralSystem.__clinics)]
        customer.setClinic(click)
        self.__curNum += 1
        self.__customers.append(customer)

        print( f"{customer.getName()} 您好！您已在{self.__name}成功挂号，序号：{customer.getNum()}，请耐心等待！")
    def getIterator(self):
        return NumeralIterator(self.__customers)


    def visit(self):
        for customer in self.__customers:
            print(f"下一位病人 {customer.getNum()}({customer.getName()}) 请到 {customer.getClinic()} 就诊")



if __name__ == '__main__':
    numeralsystem =NumeralSystem("第一人民医院挂号台")
    lily = Customer('lily')
    lily.register(numeralsystem)

    pony = Customer('pony')
    pony.register(numeralsystem)

    nick = Customer('nick')
    nick.register(numeralsystem)

    tony = Customer('tony')
    tony.register(numeralsystem)

    huahua = Customer( 'huahua' )
    huahua.register( numeralsystem )

    print()

    iterator = numeralsystem.getIterator()
    while(iterator.next()):
        customer =iterator.current()
        print(f'下一位病人{customer.getNum()}({customer.getName()}) 请到 {customer.getClinic()} 就诊')

