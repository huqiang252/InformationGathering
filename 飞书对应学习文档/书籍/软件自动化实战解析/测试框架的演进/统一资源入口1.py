#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/28


def test_new_order():
    message_id = OrderService().create_new_order(order_data)

    # wait for message to be handled
    qa_mq = QaActiveMq()
    qa_mq.wait_message_to_be_picked_up(message_id)

    order_id = qa_mq.get_order_id(message_id)

    actual_order_data = QaMySql().orders.query_by_id(order_id)
    assert actual_order_data['amount'] == order_data['amount']