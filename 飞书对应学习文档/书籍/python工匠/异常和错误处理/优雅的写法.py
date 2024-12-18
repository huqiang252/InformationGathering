#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/24


class CreateItemError(Exception):
    """创建 Item 失败"""


def create_item(name):
    """创建一个新的Item

    :raises: 当无法创建时抛出 CreateItemError
    """
    if len(name) > MAX_LENGTH_OF_NAME:
        raise CreateItemError('name of item is too long')
    if len(get_current_items()) > MAX_ITEMS_QUOTA:
        raise CreateItemError('items is full')
    return Item(name=name), ''


def create_from_input():
    name = input()
    try:
        item = create_item(name)
    except CreateItemError as e:
        print(f'create item failed: {e}')
    else:
        print(f'item<{name}> created')