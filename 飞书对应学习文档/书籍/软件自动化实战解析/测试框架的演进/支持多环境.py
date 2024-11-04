#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/29
import os
from pathlib import Path


class QaEnv:

    TEST_ENV_KEY = 'test.env'

    def __init__(self):
        self.env = self.get_env()
        self.properties = self.load_properties()

    def get_env(self):
        return os.environ.get(QaEnv.TEST_ENV_KEY)

    def load_properties(self):
        test_env = self.get_env()
        if not test_env:
            raise Exception("test.env environment variable not found")

        property_filepath = Path(__file__).parent.joinpath("properties").joinpath(test_env + ".properties")

        separator = "="
        properties = {}
        with open(str(property_filepath)) as f:
            for line in f:
                if separator in line:
                    name, value = line.split(separator, 1)
                    properties[name.strip()] = value.strip()

        return properties

    def get_property(self, property_key):
        return self.properties[property_key]