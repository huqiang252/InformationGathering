#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/2
# 文件名称   ：eventsPythonic.py


class Events:
    def __init__(self, events):
        self.events = events

    def __len__(self):
        """自定义长度，将会用来做布尔判断"""
        return len(self.events)

    def __getitem__(self, index):
        """自定义切片方法"""
        # 直接将 slice 切片对象透传给 events 处理
        return self.events[index]


if __name__ == '__main__':
    events= Events(
        [
            'computer started',
            'os launched',
            'docker started',
            'os stopped'
        ]
    )

    if events:
        print(events[1:3]) #['os launched', 'docker started']