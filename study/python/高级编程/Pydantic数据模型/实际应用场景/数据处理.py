#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024-06-25
'''
Pydantic在数据处理方面也非常有用，特别是在需要对复杂数据结构进行验证和转换的场景。
例如，处理从外部系统导入的数据时，可以使用Pydantic来确保数据的正确性和完整性
'''


from pydantic import BaseModel, ValidationError
from typing import Dict, Any

class Product(BaseModel):
    id: int
    name: str
    price: float

def process_product_data(data: Dict[str, Any]) -> Product:
    try:
        product = Product(**data)
        return product
    except ValidationError as e:
        print(e.errors())
        raise

# 示例数据
product_data = {
    "id": "123",  # 这里故意使用字符串类型来测试验证
    "name": "Laptop",
    "price": "3.15"
}

try:
    product = process_product_data(product_data)
    print(product)
except ValidationError as e:
    print("数据验证失败:", e)
