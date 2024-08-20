#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-07-27


def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return None

# 主程序
while True:
    try:
        # 获取用户输入的数值和运算符
        num1 = float(input("请输入第一个数："))
        operator = input("请输入运算符号（+、-、*、/）：")
        num2 = float(input("请输入第二个数："))

        # 调用calculate函数执行运算，并输出结果
        result = calculate(num1, num2, operator)
        if result is not None:
            print("计算结果为：", result)
        else:
            print("输入的运算符号不正确，请重新输入！")

        # 询问用户是否继续运算
        flag = input("是否继续运算？（Y/N）")
        if flag == 'N' or flag == 'n':
            break
    except ZeroDivisionError:
        print("错误：除数不能为零")
    except ValueError:
        print("错误：请输入有效的数字")
    except Exception as e:
        print("发生异常：",e)
    finally:
        print("程序结束。")
