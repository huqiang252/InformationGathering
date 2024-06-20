#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-06-20


##1.已知需求
'''
1.待测系统：jenkins
jenkins系统管理着 很多不同项目的job

权限：
大壮：系统管理员   具有所有权限
小帅：项目经理  可以给别人添加项目的job权限
大漂亮： 测试人员  可以运行测试job,终止在运行job
小美，大山，金发妹： 开发人员，可以修改job，运行job，终止在运行job

业务场景：新来测试人员：大漂亮，要加入项目

首先：大壮 在jenkins系统替大漂亮注册一个账号
然后：项目经理 小帅把大漂亮的账号，添加到 自己的项目上，并分配了测试人员权限
然后：大漂亮运行一个小帅项目下的job,名称job_1
然后：此时由于会产生冲突,小美把这job运行终止了

'''

##2.思考分析
'''
分析. 这种情况我们需要设计几个类，几个对象
===》从需求来看，该系统已知6个用户，4种用户权限，一个业务场景
（1）先设计对象
使用拟人手法来描述上面业务场景，写一段伪代码
大壮.注册账号（用户名=大漂亮）
小帅.添加权限（用户名=大漂亮，权限=测试人员权限）
大漂亮.运行job(job名=job_1)
小美.终止job(job名=job_1)


注意：添加权限，只需要添加一个权限参数；通过添加参数，然后在方法体内部if -else 就可以减少方法数量


（2）再设计类
类：
    业务类：负责业务逻辑的类，业务类里面调用工具类的对象
    工具类：负责具体实现的类，工具类的对象被业务类的方法调用




'''

##3.业务类
'''
业务类：
为了实现 大壮，小美，小帅，大漂亮，这四个对象，要设计几个类？
这四个对象，业务上来看都是jenkin系统的用户，他们能做的业务都是jenkins系统提供的业务----设计一个业务类可以处理4个对象业务
类名：Jenkins

Jenkins类主要负责对jenkins业务进行封装，不关系具体实现
如”注册账号“的封装
    . 注册账号，业务上需要几个参数
    . 注册账号，需要发送几个http请求， 每个请求http需要多少个参数， 怎样调用工具类传递这些参数


现在可以设计一个业务类jenkins，伪代码
#初始化4个对象
大壮=jenkins(用户名=大壮，密码=xxx)
小帅=jenkins(用户名=小帅，密码=xxx)
大漂亮=jenkins(用户名=大漂亮，密码=xxx)
小美=jenkins(用户名=小美，密码=xxx)


#用对象执行业务逻辑
大壮.注册账号（用户名=大漂亮）
小帅.添加权限（用户名=大漂亮，权限=测试人员权限）
大漂亮.运行job(job名=job_1)
小美.终止job(job名=job_1)
'''

##4.工具类
'''
我们已知 jenkins系统的各种业务都可以调用http api接口来实现，那么jenkins类的方法到底怎样发送http请求和解析http api的响应
显然 这个跟jenkins业务无关，应该交给专门负责http请求的类来负责
类名：RestClient
这个类 是工具类 ,是发送 和 接受http请求的工具

工具类的实例：应该组合到 jenkins类的初始化内部，这样jenkins里面所有涉及到Http请求的地方，都调用这个实例来做

伪代码如下



jenkins 类可以有一些更加复杂的业务方法，比如要调用多个接口的业务方法。
这种复杂业务方法的封装。。。后续

关于参数：
    通常都是简单数据类型，比如 字符串，整数之类，如果参数过多，我们还需要对其简化
    例如有点业务方法有几十个参数，那么这十几个参数可以结合为一个复杂数据类型的参数
    def 某个方法(username,payload):
        return self.rest_client.post(usr=xxx,json=payload)

'''


class Jenkins:
    def __init__(self, username, password):
        self.rest_client = RestClient()
        self.rest_client.xxxx = xxxxxxx  # 做一些配置

    def 注册账号(self, username, xxxx):
        payload = {'username': username, 'xxxx': xxxx}
        return self.rest_client.post(url=xxx, json=payload)

    def 添加权限(self, username, previlege):
        payload = {'username': username, 'previlege': previlege}
        return self.rest_client.post(url=xxx, json=payload)


##5.错误的设计：过多的业务类
'''
需求中的4种用户权限，如果给每种用户设计一个类可以么？ 理论可以，实际不可行
既然每种用户权限能调用接口不同，那么直接些5个类
JenkinsAdmin 管理员
JenkinsProjectManager
JenkinsDeveloper 表示开发
JenkinsQA 表示测试
Jenkins 用作父类  包含公共逻辑
然后 每个类只包含自己能调用的接口，大家都能调用的接口放在父类Jenkins里面

出现如下问题：
    1.类过多，每个类都小，违反“类要深”的原则
    2.逻辑非常复杂，且类之间有重复，每次新增一个方法，可能要复制好份，放在不同角色里面
    3.没有任何明显的收益，一个类搞成5个类，代码数量凭空变多。好处没有。

    而且：我们经常需要做反向测试，比如：测试以下QA是否真的不能修改全局系统配置，放在5个类的设计反而做不了

    另外，我们可以接受业务类的简单分层

'''

##6.类可以组合多个对象
'''
我们把思考扩展下，jenkins类内部可以组合更多对象
比如SeleniumClien类的对象，这样jenkins类具备了图形界面实现业务的功能

还可以组合一个SSHClient类的对象，支持修改服务端文件的功能


'''


class Jenkins:
    def __init__(self, username, password):
        self.rest_client = RestClient()
        self.selenium_client = SeleniumClient()
        self.ssh_client = SSHClient()
        ...


