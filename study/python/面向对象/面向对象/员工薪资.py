#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-07-28
#创建员工类
class Employee:
    def __init__(self, hours, hourly_rate):
        self.hours = hours
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        pass


#创建全职员工类
class FullTimeEmployee(Employee):
    def __init__(self, hours, hourly_rate):
        super().__init__(hours, hourly_rate)  # 调用父类的构造方法来初始化属性

    def calculate_salary(self):
        return self.hours * self.hourly_rate  # 根据工时和时薪计算薪资

#创建兼职员工类
class PartTimeEmployee(Employee):
    def __init__(self, hours, hourly_rate):
        super().__init__(hours, hourly_rate)  # 调用父类的构造方法来初始化属性

    def calculate_salary(self):
        return self.hours * self.hourly_rate  # 根据工时和时薪计算薪资

full_time_employee = FullTimeEmployee(160, 100.5)  # 创建一个全职员工对象假设工作时长是160小时，薪资是100小时
full_time_salary = full_time_employee.calculate_salary()  # 调用全职员工对象的计算薪资方法
print("全职员工的薪资是:", full_time_salary)  # 打印全职员工的薪资

part_time_employee = PartTimeEmployee(80, 50)  # 创建一个兼职员工对象
part_time_salary = part_time_employee.calculate_salary()  # 调用兼职员工对象的计算薪资方法
print("兼职员工的薪资是:", part_time_salary)  # 打印兼职员工的薪资
