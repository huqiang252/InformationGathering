#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/27


class LeftTicketPage:
    PAGE_URL = 'https://kyfw.12306.cn/otn/leftTicket/init'

    #在实现了它的初始化函数和析构函数之后，我们可以保证在创建PO类对象的时候，相应的底层Web Driver实例会被创建好，
    # 在这个PO类对象被销毁的时候，相应的Web Driver实例会被关闭
    def __init__(self):
        self.browser = webdriver.Chrome(executable_path=chromedriver_binary_path)
        self.browser.get(LeftTicketPage.PAGE_URL)

    def __del__(self):
        if self.browser:
            self.browser.close()

    def _select_station_from_pop_list(self, city_name):
        elements = self.browser.find_elements_by_css_selector("ul.popcitylist > li")
        for elem in elements:
            if elem.text == city_name:
                elem.click()
                return

        raise Exception("Not able to find {} from pop city list", city_name)

    def select_station_from(self, station_name):
        self.browser.find_element_by_id('fromStationText').click()
        self._select_station_from_pop_list(station_name)

        return self



def test_train_type_filter():
    page = LeftTicketPage()

    page.select_station_from('上海')
    page.select_station_to('北京')
    page.select_departure_date(1)

    all_trains = page.get_displayed_trains()

    page.select_train_type('T')
    filtered_trains = page.get_displayed_trains()

    for train in all_trains:
        if train.startswith('T'):
            assert train in filtered_trains

    for train in filtered_trains:
        assert train.startswith('T')
