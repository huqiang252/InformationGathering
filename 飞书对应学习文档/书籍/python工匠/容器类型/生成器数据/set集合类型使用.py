#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/24


#注意：这里的示例列表很短，所以转不转集合对性能的影响可能微乎其微
# 在实际编码时，列表越长、执行的判断次数越多，转成集合的收益就越高
VALID_NAMES = ["piglei", "raymond", "bojack", "caroline"]
# 转换为集合类型专门用于成员判断
VALID_NAMES_SET = set(VALID_NAMES)

def validate_name(name):
    if name not in VALID_NAMES_SET:
        raise ValueError(f"{name} is not a valid name!")


if __name__ == '__main__':
    validate_name("bojack")
    validate_name('sljf')