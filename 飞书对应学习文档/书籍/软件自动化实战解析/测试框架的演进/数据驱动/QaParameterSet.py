#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/29
import pytest
from _pytest.mark import ParameterSet, MarkDecorator
import yaml

class QaParameterSet(ParameterSet):
    @classmethod
    def dict_param(cls, *values, marks=()):
        if isinstance(marks, MarkDecorator):
            marks = (marks,)
        else:
            assert isinstance(marks, (tuple, list, set))

        return cls(values, marks, values[0]['description'])

    @classmethod
    def yml_params(cls, yml_path=''):
        with open(yml_path, 'r',encoding='utf-8') as f:
            # tests = yaml.load_all(f,yaml.FullLoader)
            tests = yaml.safe_load(f)

            test_definitions = []
            for test_case in tests:
                test_definitions.append(QaParameterSet.dict_param(test_case))

        return test_definitions


def remove_whitespaces(input_str):
    # a buggy implementation
    return input_str.strip()


class TestDefinition:

    def __init__(self):
        self.description = ''
        self.priority = ''
        self.input = ''
        self.expected = ''

    @classmethod
    def from_dict(cls, dict_data):
        obj = cls()
        obj.description = dict_data['description']
        obj.priority = dict_data['priority']
        obj.input = dict_data['input']
        obj.expected = dict_data['expected']

        return obj



@pytest.mark.parametrize("test_definition", QaParameterSet.yml_params('resources/tests.yml'))
def test_remove_whitespaces(test_definition):
    test_definition = TestDefinition.from_dict(test_definition)
    actual = remove_whitespaces(test_definition.input)
    assert actual == test_definition.expected


# @pytest.mark.parametrize("test_definition", QaParameterSet.yml_params('resources/tests.yml'))
# def test_remove_whitespaces(test_definition):
#     actual = remove_whitespaces(test_definition['input'])
#     assert actual == test_definition['expected']