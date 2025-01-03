#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员： qiang.hu
# datetime： 2024/12/20
# 文件名称   ：组合代码.py


from abc import ABC, abstractmethod

class Component(ABC):
    """组件"""

    def __init__(self, name):
        self._name = name

    def get_name(self):
        """获取组件名称"""
        return self._name

    def is_composite(self):
        """判断是否为复合组件"""
        return False

    @abstractmethod
    def check(self, indent=""):
        """
        检查组件
        :param indent: 缩进字符串，用于格式化输出
        """
        pass

class Item(Component):
    """普通商品"""

    def check(self, indent=""):
        """
        检查普通商品
        :param indent: 缩进字符串，用于格式化输出
        """
        print(f"{indent}Checking item: {self.get_name()}")

class CombineItem(Component):
    """组合商品"""

    def __init__(self, name):
        super().__init__(name)
        self._components = []

    def add_component(self, component):
        """添加子组件"""
        self._components.append(component)

    def remove_component(self, component):
        """移除子组件"""
        self._components.remove(component)

    def is_composite(self):
        """判断是否为复合组件"""
        return True

    def check(self, indent=""):
        """
        检查组合商品及其子商品
        :param indent: 缩进字符串，用于格式化输出
        """
        print(f"{indent}Checking combine item: {self.get_name()}")
        indent += "\t"
        for component in self._components:
            component.check(indent)

# 示例用法
if __name__ == "__main__":
    laptop = Item("Laptop")
    mouse = Item("Mouse")

    electronics = CombineItem("Electronics")
    electronics.add_component(laptop)
    electronics.add_component(mouse)

    fridge = Item("Fridge")
    microwave = Item("Microwave")
    home_appliances = CombineItem("Home Appliances")
    home_appliances.add_component(fridge)
    home_appliances.add_component(microwave)

    store = CombineItem("Store")
    store.add_component(electronics)
    store.add_component(home_appliances)

    store.check()
