#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2025/1/5
# 文件名称   ：值对象.py


from dataclasses import dataclass
from typing import NamedTuple
from collections import namedtuple


@dataclass(frozen=True)
class Name:
    first_name: str
    surname: str


class Money(NamedTuple):
    currency: str
    value: int


Line = namedtuple('Line', ['sku', 'qty'])


def test_equality():
    assert Money('gbp', 10) == Money('gbp', 10)
    assert Name('Harry', 'Percival') != Name('Bob', 'Gregory')
    assert Line('RED-CHAIR', 's') == Line('RED-CHAIR', 's')

def test_name_equality():
    assert Name("张三","aa") != Name("李四","bb")


class Person:
    def __init__(self, name: Name):
        self.name = name


def test_barry_is_harry():
    harry = Person(Name("张三",'aa'))
    barry = harry
    barry.name = Name("李四",'bb')
    assert harry is barry and barry is harry


import pytest
fiver = Money('gbp', 5)
tenner = Money('gbp', 10)


def can_add_money_values_for_the_same_currency():
    assert fiver + fiver == tenner


def can_subtract_money_values():
    assert tenner - fiver == fiver


def adding_different_currencies_fails():
    with pytest.raises(ValueError):
        Money('usd', 10) + Money('gbp', 10)


def can_multiply_money_by_a_number():
    assert fiver * 5 == Money('gbp', 25)


def multiplying_two_money_values_is_an_error():
    with pytest.raises(TypeError):
        tenner * fiver


if __name__ == '__main__':
    can_multiply_money_by_a_number()