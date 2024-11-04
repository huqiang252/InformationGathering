#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-10-28


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

    def finished(self):
        if self.succeeded() or self.failed():
            return True

        return False