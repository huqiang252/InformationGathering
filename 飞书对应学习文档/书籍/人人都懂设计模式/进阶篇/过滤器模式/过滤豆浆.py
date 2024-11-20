#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/11/10


class FilterScreen:
    """过滤网"""

    def doFilter(self, rawMaterials):
        for material in rawMaterials:
            if (material == "豆渣"):
                rawMaterials.remove(material)
        return rawMaterials


if __name__ == '__main__':
    rawMaterials = ["豆渣", "豆沙", "豆沙", "豆沙", "豆沙", "豆沙", "豆沙", "豆沙", "豆沙", "豆沙", "豆沙", "豆沙", "豆沙", "豆沙", "豆沙", "豆沙", "豆沙", "豆沙", "豆沙","豆沙", "豆沙", "豆沙", "豆沙",]
    print("过滤前：", rawMaterials)
    filter=FilterScreen()
    filteredMaterials=filter.doFilter(rawMaterials)
    print("过滤后：", filteredMaterials)