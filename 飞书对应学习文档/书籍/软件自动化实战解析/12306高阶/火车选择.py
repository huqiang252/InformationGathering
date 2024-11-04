#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/29


def select_train_type(self, train_type_enum):
    print("Select train type by '{}'".format(train_type_enum.name))
    elem = self.browser.find_element_by_css_selector(
        "#_ul_station_train_code > li > input.check[value='{}']".format(train_type_enum.value))

    if not elem.is_selected():
        elem.click()

    return self


from enum设计 import TrainTypeEnum
def test_train_type_filter():
    ...
    filter_train_type = TrainTypeEnum.TeKuai
    page.select_train_type(filter_train_type)

    ...

    for train in filtered_trains:
        assert train.startswith(filter_train_type.value)