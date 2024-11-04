#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/28


def test_new_order(resources):
    message_id = resources.order_service.create_new_order(order_data)

    # wait for message to be handled
    resources.mq.wait_message_to_be_picked_up(message_id)

    order_id = resources.mq.get_order_id(message_id)

    actual_order_data = resources.database.orders.query_by_id(order_id)
    assert actual_order_data['amount'] == order_data['amount']