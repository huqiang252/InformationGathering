#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/27


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class LeftTicketPage:

    def get_displayed_trains(self):
        WebDriverWait(self.browser, 20).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "#queryLeftTable > tr.bgc")))

        trains = []
        elements = self.browser.find_elements_by_css_selector("#queryLeftTable > tr")
        for elem in elements:
            train_info = elem.get_attribute("datatran")
            if not train_info:
                continue

            trains.append(train_info)

        return trains