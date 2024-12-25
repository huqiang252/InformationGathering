#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/17
# 文件名称   ：cqrs_main.py
# main.py
from command_handlers import CommandHandler
from event_handlers import Inventory
from query_handlers import QueryHandler
from commands import AddProduct

# 初始化处理器
command_handler = CommandHandler()
inventory = Inventory()
query_handler = QueryHandler(inventory)

# 处理命令
commands = [
    AddProduct("p1", "Laptop", 10),
    AddProduct("p2", "Smartphone", 20)
]

for command in commands:
    events = command_handler.handle(command)
    for event in events:
        inventory.apply_event(event)

# 处理查询
queries = [
    "get_inventory",
    "get_product_quantity:p1"
]

for query in queries:
    result = query_handler.handle(query)
    print(result)
