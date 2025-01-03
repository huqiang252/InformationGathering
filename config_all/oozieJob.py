#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/22
# 文件名称   ：oozieJob.py
class OozieJob:
    def __init__(self):
        self.status = ''
        ...

    def succeeded(self):
        if not self.status:
            return False

        if self.status.lower() in ['success', 'succeeded', 'ok']:
            return True

        return False

    def failed(self):
        if not self.status:
            return False

        if self.status.lower() in ['fail', 'failed']:
            return True

        return False


#在这个基础上，我们还可以为这样的类加上扩展的方法，方便自动化测试用例的使用
    def finished(self):
        if self.succeeded() or self.failed():
            return True

        return False