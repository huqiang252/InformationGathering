#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-06-21

##1.测试分析vs 测试设计

#文档： https://blog.csdn.net/hlsxjh/article/details/143515819

'''
测试分析 = 测试指导思想
测试设计 = 测试指导行动

思想指导行动->测试分析指导测试设计
测试分析回答测试什么？
测试设计回答如何测试？
'''


##2.测试分析模型
'''
产品级测试分析
    目标理解系统整体功能，优先级和依赖
    促进测试计划和测试策略的设计，回归测试计划打下基础
    
    
功能级测试分析
    理解特定功能需求
    运用测试设计方法 
'''


#3.产品级测试分析
'''
产品级测试分析
    分解：将系统分解高级模块
        
    优先级：根据业务需求和业务目标确定系统功能的重要性
    
    依赖分析：识别系统中特性之间的关系
(1)分解
    步骤
        1.定义对象
            objects:
                Users
                workspaces
                Channels
                Messages
            Epics
                Permissions
                Help
                History
                Search
        2.为每个对象定义行为
             objects:
                Users
                    actions:
                        invite
                        create account
                        Deactivate
                        ..
                workspaces
                    actions:
                        create
                        Customize
                        ...
                Channels
                Messages
        3.定义行为的替代方法（在系统中，执行相同操作可以不同方式，这一点要注意）
                objects:
                    channels
                        actions:
                            create
                                methods:
                                    workspace menu option
                                    channels section menu option
                                    ....
                            join
                            Leave
                            
(2)优先级
列出优先级列表
    开始测试更重要的功能
    尽早发现更关键的BUG
    创建不同测试套件
    
为每个对象和每个行为设置优先级
objects:
    channels  //实例对象
        actions: //动作
            create
                methods:  //替代方法
                    workspace menu option
                    channels section menu option
                    ....
                Priorities:  //优先级
                    Critical
            join
            Leave

                            
                    
(3)依赖分析
识别依赖有助于：
    识别系统的相关功能，确保在测试期间覆盖所有必要的场景
    识别特定功能的变更对其他功能的潜在影响
    评估影响，并执行针对性测试缓解此类风险

回顾我们的对象，思考他们如何相互作用，寻找任何依赖关系
    函数依赖关系：一个对象依赖于另一个对象的输出或行为
    数据依赖性：一个对象需要来自于另一对象的特定数据
    
定义对象之间的依赖关系
    双向矩阵
        哪些项目依赖其他项目
        哪些项目被其他项目所依赖
'''



##4.功能级测试分析
'''
功能级有三个主要的测试分析活动
    被测对象的分解
    测试设计（使用恰当的测试设计技术创建测试用例）
    依赖分析（定义测试特性与系统中其他特性之间的关系）

（1）分解
对于功能测试分析，需要进一步定义被测对象的参数
参数是对象的属性或者特征，基本上参数是作为输入的值，为特定操作提供所需的特定信息
步骤
    1.定义对象和动作
        对象：用户
        操作：创建用户
    2.定义动作的参数
    如用户提交一个表单，来创建账户
        用户名（string)
        密码(必传）
        电子邮件（默认）
    3.为每个参数定义测试数据
        有效测试数据集

（2）测试设计
    测试数据验证
        等价类划分
        边界值分析
        组合测试
    核心是关注测试业务逻辑功能的方法
        状态转移测试
        决策表
(3) 依赖分析
步骤
    1.找到对象
        object:
            users
            workspaces
            channels
            messages
            
    2.定义相关对象的状态
        channels: active,archived,deleted
        users:active,archived,deleted
    3.定义相关对象的参数
        channels: public,private
        users:普通用户，访客，外部用户
        
    设计功能测试，组合 状态+参数
    
    
'''