#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/17
# 文件名称   ：command_handlers.py


# command_handlers.py
from events import ProductAdded
from commands import AddProduct

class CommandHandler:
    def handle(self, command):
        if isinstance(command, AddProduct):
            event = ProductAdded(command.product_id, command.name, command.quantity)
            return [event]
        else:
            raise ValueError("Unsupported command")
