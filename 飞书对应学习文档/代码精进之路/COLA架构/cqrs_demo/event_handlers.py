#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/17
# 文件名称   ：event_handlers.py.py

from events import ProductAdded

# event_handlers.py
class Inventory:
    def __init__(self):
        self.products = {}

    def apply_event(self, event):
        if isinstance(event, ProductAdded):
            if event.product_id in self.products:
                self.products[event.product_id]['quantity'] += event.quantity
            else:
                self.products[event.product_id] = {'name': event.name, 'quantity': event.quantity}
        else:
            raise ValueError("Unsupported event")

    def get_product_quantity(self, product_id):
        return self.products.get(product_id, {}).get('quantity', 0)
