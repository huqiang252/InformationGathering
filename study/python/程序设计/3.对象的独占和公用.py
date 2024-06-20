#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-06-20


##1.业务类 vs 其他封装方式
'''
1. 独占对象
    每一个jenkins类创建----创建组合在内的RestClient对象
    不同的jenkins对象之间，这些RestClient对象互相对立，互不影响，才有有不同的headers，保持不同的token和session


2. 公用对象
公用对象  =  唯一的
数据库操作类DBManager 放在db.py文件中
    若在外边创建一个类对象dbm,那么之后所有地方，都需要导入这个对象from db import dbm

    用拟人化思想来看这个实现，那就是有一个专门的数据库管理员，由于不存在多个数据库管理员，则数据库管理员 和数据库之间的链接只有一个
    这样可以降低测试时 对数据库链接数的占用
'''