#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/22
# 文件名称   ：qaLogger.py
class QaLogger:

    def __init__(self):
        self._step_index = 0
        self._last_log = None

    def info(self, text):
        print(text)
        self._last_log = text

    def step(self, text):
        self._step_index += 1
        print('\nStep {}: {}'.format(self._step_index, text))
        self._last_log = text

    def step_done(self):
        print('Step {}  done!'.format(self._step_index))




