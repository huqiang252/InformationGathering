#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-06-21
##1.需求分析
'''
1.涉及哪些系统？
客户端：app，pc
切源管理台
切源对外系统
切源规则对象lcm

切源管理台的能力
    源管理
        展业地由后端返回，后台从nacos配置中获取
        [{"areaCode":"MAS","areaCnName":"马来","seq":"02"},{"areaCode":"HK","areaCnName":"香港","seq":"01"},{"areaCode":"SGP","areaCnName":"新加坡","seq":"03"}]
    站点管理
    切源管理
    切源记录
    配置推送


切源对外系统的能力
    APP/PC 获取配置信息
    统一行情获取配置

2.业务需求
(1)hq-monitor,prometheus,zabbix 收集log
(2)log  存储在ELK系统
(3)LCM 根据规则，触发规则回调
(4)回调通知到 切源管理台
    TODO:lcm相关接口?
    一个是查询，用来查询规则
    一个是回调：告警触发调行情接口--切源管理台进行切源判断


(5)切源管理台
    根据切源管理，判断是否切源，不切源exit
    确定切源，判断权限认证是否成功，不成功exit
    权限认证成功，进行切源处理------（TODO: 万一切源处理失败了，是否可以回滚）
    切源处理成功后，同步发送消息推送----（TODO: 发送消息万一失败了，怎么处理；发送消息的及时性如何验证？）
    消息发送成功后，发送告警
    成功告警后，流水记录，入数据库
        hs_hq_admin.site_switch_log  切换流水表
'''








