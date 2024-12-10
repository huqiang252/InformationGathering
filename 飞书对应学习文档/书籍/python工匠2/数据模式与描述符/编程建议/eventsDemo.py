#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/2
# 文件名称   ：eventsDemo.py


class Events:
    def __init__(self,events):
        self.events = events


    def is_empty(self):
        return not bool(self.events)


    def list_event_by_range(self,start,end):
        return self.events[start:end]


if __name__ == '__main__':
    events= Events(
        [
            'computer started',
            'os launched',
            'docker started',
            'os stopped'
        ]
    )

    if not events.is_empty():
        print(events.list_event_by_range(1,3)) #['os launched', 'docker started']
