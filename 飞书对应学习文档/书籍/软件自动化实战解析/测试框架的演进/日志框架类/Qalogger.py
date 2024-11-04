#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/29


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