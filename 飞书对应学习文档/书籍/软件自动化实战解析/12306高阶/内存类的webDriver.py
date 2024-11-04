#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/30


from selenium.webdriver.chrome.webdriver import WebDriver as GoogleWebDriver
from chromedriver_py import binary_path as chromedriver_binary_path

class ChromeDriver:

    class __ChromeDriver(GoogleWebDriver):
        def __init__(self):
            super().__init__(executable_path=chromedriver_binary_path)

        # more methods ....

    __instance = None

    def __new__(cls):
        if not ChromeDriver.__instance:
            ChromeDriver.__instance = ChromeDriver.__ChromeDriver()

        return ChromeDriver.__instance