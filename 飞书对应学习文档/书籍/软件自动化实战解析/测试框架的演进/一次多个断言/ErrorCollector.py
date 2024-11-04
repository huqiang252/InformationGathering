#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/29


class ErrorCollector:

    def __init__(self):
        self.errors = []

    def assert_equals(self, actual, expected, error_description):
        if actual == expected:
            return

        error_description += '\n    actual:   {}\n    expected: {}'.format(actual, expected)
        self.errors.append(error_description)

    def assert_string_contains(self):
        pass

    def assert_list_contains(self):
        pass

    def evaluate(self):
        if not self.errors:
            return

        joint_error_message = '{} assertion failures found:'.format(len(self.errors))
        for error in self.errors:
            joint_error_message += '\n  - ' + error

        raise AssertionError(joint_error_message)


def test_error_collector():

    error_collector = ErrorCollector()

    error_collector.assert_equals(1 + 2, 4, 'addition does not work')
    error_collector.assert_equals(6 - 2, 4, 'deduction does not work')
    error_collector.assert_equals(2 * 3, 6, 'times does not work')
    error_collector.assert_equals(8 / 4, 5, 'division does not work')

    error_collector.evaluate()