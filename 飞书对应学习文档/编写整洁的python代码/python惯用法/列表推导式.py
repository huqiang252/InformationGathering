#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2025/1/12
# 文件名称   ：列表推导式.py


from typing import Iterable, Set
import re
ARN_REGEX= re.compile(r"arn:([^:]+):([^:]+):([^:]+):([^:]+):([^:]+)")
def collect_account_ids_from_arns(arns: Iterable[str]) -> Set[str]:
    """Given several ARNs in the form

        arn:partition:service:region:account-id:resource-id

    Collect the unique account IDs found on those strings, and return them.
    """
    collected_account_ids = set()
    for arn in arns:
        matched = re.match(ARN_REGEX, arn)
        if matched is not None:
            account_id = matched.groupdict()["account_id"]
            collected_account_ids.add(account_id)
    return collected_account_ids




def collect_account_ids_from_arns(arns):
    matched_arns = filter(None, (re.match(ARN_REGEX, arn) for arn in arns))  #re.match(ARN_REGEX, arn) 尝试将 arn 与 ARN_REGEX 正则表达式进行匹配，返回一个匹配对象或 None
    return {m.groupdict()["account_id"] for m in matched_arns}



def collect_account_ids_from_arns(arns: Iterable[str]) -> Set[str]:
    return {
        matched.groupdict()["account_id"]
        for arn in arns
        if (matched := re.match(ARN_REGEX, arn)) is not None  #使用海象运算符 := 将 re.match(ARN_REGEX, arn) 的结果赋值给 matched，并检查是否为 None。
    }