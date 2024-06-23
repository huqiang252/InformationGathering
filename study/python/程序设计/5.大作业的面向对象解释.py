#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-06-21

##1.面向对象程序的设计
'''
(1) 类的外部接口 设计要抽象而简单
    外部接口：从类的外部调用类的方法时要传的参数的复杂程度
(2) 类要深

1.1类的对象外部接口要抽象且简单
乔布斯一句话： 对象就想人一样，也是活生生的生命
优点：
    当具体实现发送变化时，绝大部分接口调用都不需要改。 我们尽可能让外部接口设计只包含业务含义，不包含具体实现


外部接口怎么做到 抽象且简单呢？
    尽可能增加带默认值的参数。 给外部接口设计默认逻辑和特殊逻辑
    普通用户：默认逻辑
    高级用户：通过传参来使用特殊逻辑，你可以自己查文档传特殊的参数

1.2 类要深
我们需求接口简单且抽象，但是功能强大的类。
    如：unix操作系统提供的文件读写接口
        屈指可数的几个参数，代码功能非常强大，代码行数非常多

    更加厉害的接口设计，则根本没有参数，也不用你调用，全自动，比如：JVM里面的垃圾回收机制，不提供接口给用户
'''

##2.大作业的面向对象解答
import os
import argparse
class CSVHandler:
    #工具类
    def __int__(self,raw):
        self.lines = self.read_csv_lines(raw)

    def read_csv_lines(self,input_csv):
        '''

        :param input_csv: 如果传入是文件名，那么读文件，如果是传入字符串，就直接保存
        :return:
        '''
        result =[]
        if input_csv.lower().endswith(".csv") and os.path.exists(input_csv):
            with open(input_csv,"r",encoding="utf-8") as f:
                temp  = f.readlines()
            for _ in temp:
                result.append(_.split(","))
        else:
            result.append(input_csv.split(","))
        return result
    def multiply(self,field,multipler):
        for line in self.lines:
            try:
                line[field-1] = float(line[field-1])
                line[field-1] *= multipler
                line[field-1]= round(line[field-1],5)
            except:
                #使用try except为了让csv文件第一行表头在乘法不会做任何变动，这样调用者不用区分含有表头还是不含表头
                pass
    def add_sign(self,field,sign):
        for line in self.lines:
            try:
                float(line[field-1])
                line[field-1]=sign+str(line[field-1])
            except:
                pass

    def remove_sign(self,field,sign):
        for line in self.lines:
            line[field-1] = line[field-1].replace(sign,"")

    def output(self,output_csv):
        if output_csv.lower().endswith(".csv"):
            with open(output_csv,"w",encoding="utf-8") as f:
                for line in self.lines:
                    f.write(",".join(line))
        else:
            for line in self.lines:
                print(",".join(line),end="")


class CurrencyConverter:
    #业务类
    def __int__(self,input_csv,field,multipler,output_csv,from_sign="",to_sign="$"):
        self.input_csv=input_csv
        self.field = int(field)
        self.multipler=float(multipler)
        self.output_csv= output_csv
        self.csv_handler=CSVHandler(input_csv)  #小帅的类的初始化方法里面让小美待命
        self.from_sign=from_sign
        self.to_sign= to_sign

    def covert(self):
        self.csv_handler.remove_sign(self.field,self.from_sign)
        self.csv_handler.multiply(self.field,self.multipler)
        self.csv_handler.add_sign(self.field,self.to_sign)
        self.csv_handler.output(self.output_csv)



if __name__ == '__main__':
    '''命令行处理部分'''
    parser = argparse.ArgumentParser(prog="current_convert",
                                     usage="%(prog)s <--field N> [--multiplier N] [-i input] [-o output]"
                                     )
    parser.add_argument("--field",required=True,metavar="N",help="价格信息在csv文件的第N列，需要进行转换")
    parser.add_argument("--multiplier",default=0.8,metavar="N",help="转换方法吧当前的数值乘以N,这个N表示汇率")
    parser.add_argument("-i",metavar="input",help="从input文件内读取CSV文件内容(或者从stdin读取")
    parser.add_argument("-o",metavar="output",default="",help="输出到output文件中（或者输出到stout)")
    args = parser.parse_args()
    converter = CurrencyConverter(args.i,args.field,args.multiplier,args.o)
    converter.covert()



#2.类的组合
'''
不要动不动就继承，要学会对象的组合
组合模式
把CurrencyConverter类的实例比作一个人，叫小帅
小帅只知道汇率转换的业务逻辑：
1.移除原本的货币符号
2.做乘法运算
3.增加新的货币符号
4.输出结果


把CSVHandler类的实例，叫小美
小美只知道怎样处理csv文件
1.读取csv文件
2.对csv文件的每一行的指定字段做乘法
3.给csv的每一行的指定字段前面添加一个特定符号
4.给csv的每一行的指定字段前面删除一个特定符号
5.删除csv文件

拟人手法
    有小帅+小美，需求：要对放在csv文件里面的汇率数据做汇率转换，如何做？
    小帅：汇率换算组长
    小美：小组成员
    小帅的类的初始化方法里面让小美待命
'''