#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/17
# 文件名称   ：query_handlers.py.py

# query_handlers.py
class QueryHandler:
    def __init__(self, inventory):
        self.inventory = inventory

    def handle(self, query):
        if query == "get_inventory":
            return self.inventory.products
        elif query.startswith("get_product_quantity"):
            product_id = query.split(":")[1]
            return self.inventory.get_product_quantity(product_id)
        else:
            raise ValueError("Unsupported query")
