#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-07-27
# 定义房子类
class House:
  def __init__(self, house_type, total_area):
    self.house_type = house_type # 户型
    self.total_area = total_area # 总面积
    self.furniture = [] # 家具列表

  # 添加家具
  def add_furniture(self, furniture):
    if self.total_area >= furniture.area: # 判断剩余面积是否足够
      self.furniture.append(furniture) # 添加家具到家具列表
      self.total_area -= furniture.area # 更新剩余面积
      print(f"{furniture.name}已添加到房子中")
    else:
      print(f"房子剩余面积不足，无法添加{furniture.name}")

  # 展示房子信息
  def display(self):
    # 打印户型
    print("户型:", self.house_type)
    # 打印总面积
    print("总面积:", self.total_area, "平米")
    # 打印剩余面积
    print("剩余面积:", self.total_area, "平米")
    # 打印家具名称列表
    print("家具名称列表:")
    for furniture in self.furniture:#循环遍历家具列表，打印出每个家具的名字
      print(furniture.name)


# 定义家具类
class Furniture:
  def __init__(self, name, area):
    self.name = name # 家具名称
    self.area = area # 家具占地面积


# 创建房子对象
my_house = House("两室一厅", 100)

# 创建家具对象
bed = Furniture("床", 4)
wardrobe = Furniture("衣柜", 2)
table = Furniture("餐桌", 1.5)

# 添加家具到房子中
my_house.add_furniture(bed)
my_house.add_furniture(wardrobe)
my_house.add_furniture(table)

# 打印房子信息
my_house.display()
