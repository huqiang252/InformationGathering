#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2025/1/4
# 文件名称   ：事件驱动.py


class Event:
    def __init__(self, name, data=None):
        self.name = name
        self.data = data

class EventBus:
    def __init__(self):
        self.handlers = {}

    def subscribe(self, event_name, handler):
        if event_name not in self.handlers:
            self.handlers[event_name] = []
        self.handlers[event_name].append(handler)

    def publish(self, event):
        if event.name in self.handlers:
            for handler in self.handlers[event.name]:
                handler(event.data)

def handle_order_created(data):
    print(f"Handling order created: {data}")


def handle_order_xxx(data):
    print(f"Handling order xxx: {data}")

def handle_payment_received(data):
    print(f"Handling payment received: {data}")

event_bus = EventBus()
event_bus.subscribe('order.created', handle_order_created)
event_bus.subscribe('order.created', handle_order_xxx)
event_bus.subscribe('payment.received', handle_payment_received)

event_bus.publish(Event('order.created', {'orderId': '123'}))
event_bus.publish(Event('payment.received', {'orderId': '123', 'amount': 100}))

