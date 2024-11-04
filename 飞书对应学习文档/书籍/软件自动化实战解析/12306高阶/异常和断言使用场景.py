#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/30

class TestLeftTicketPage:

    def test_train_filter(self):
        page = LeftTicketPage()

        page.select_station_from('上海')
        page.select_station_to('北京')
        page.select_departure_date(1)

        all_trains = page.get_displayed_trains()

        filter_train_type = TrainTypeEnum.TeKuai

        page.select_train_type(filter_train_type)
        filtered_trains = page.get_displayed_trains()

        for train in all_trains:
            if train.startswith(filter_train_type.value):
                assert train in filtered_trains

        for train in filtered_trains:
            assert train.startswith(filter_train_type.value)