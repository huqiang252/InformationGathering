#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/22
# 文件名称   ：一次断言多个错误.py


class ErrorCollector:

    #软断言（优化）20241113
    '''
    优化方式：
    error_collector = ErrorCollector()
    error_collector.assert_equals( 1 + 2, 4, 'addition does not work' )
    error_collector.assert_equals( 6 - 2, 3, 'deduction does not work' )
    error_collector.evaluate()

    '''
    def __init__(self):
        self.errors = []

    def assert_condition(self, condition, error_description):
        if not condition:
            self.errors.append(error_description)

    def assert_equals(self, actual, expected, error_description):
        self.assert_condition(actual == expected, error_description + '\n    actual:   {}\n    expected: {}'.format(actual, expected))

    def assert_not_equals(self, actual, expected, error_description):
        self.assert_condition(actual != expected, error_description + '\n    actual:   {}\n    expected: {}'.format(actual, expected))

    def assert_true(self, value, error_description):
        self.assert_condition(value, error_description + '\n    value:    {}'.format(value))

    def assert_false(self, value, error_description):
        self.assert_condition(not value, error_description + '\n    value:    {}'.format(value))

    def assert_greater_than(self, actual, expected, error_description):
        self.assert_condition(actual > expected, error_description + '\n    actual:   {}\n    expected: {}'.format(actual, expected))

    def assert_less_than(self, actual, expected, error_description):
        self.assert_condition(actual < expected, error_description + '\n    actual:   {}\n    expected: {}'.format(actual, expected))

    def assert_none(self, value, error_description):
        self.assert_condition(value is None, error_description + '\n    value:    {}'.format(value))

    def assert_not_none(self, value, error_description):
        self.assert_condition(value is not None, error_description + '\n    value:    {}'.format(value))

    def assert_string_contains(self, substring, string, error_description):
        self.assert_condition(substring in string, error_description + '\n    string:   {}\n    substring: {}'.format(string, substring))

    def assert_list_contains(self, element, list_, error_description):
        self.assert_condition(element in list_, error_description + '\n    list:     {}\n    element:  {}'.format(list_, element))

    def evaluate(self):
        if not self.errors:
            return

        joint_error_message = '发现{}个断言失败:'.format(len(self.errors))
        for error in self.errors:
            joint_error_message += '\n  - ' + error

        raise AssertionError(joint_error_message)


if __name__ == '__main__':
    error_collector = ErrorCollector()
    error_collector.assert_equals( 1 + 2, 4, 'addition does not work' )
    error_collector.assert_equals( 6 - 2, 3, 'deduction does not work' )
    error_collector.assert_equals( 2 * 3, 6, 'times does not work' )
    error_collector.assert_equals( 8 / 4, 2, 'division does not work' )
    error_collector.assert_list_contains( 'x', ['a', 'b', 'c'], 'list does not contain element')
    error_collector.evaluate()