#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/26


from openpyxl import load_workbook

excel_file = 'tests.xlsx'
workbook = load_workbook(filename=excel_file)

#1.workbook对象有一个属性，叫作worksheets，这是一个list，里面的元素是这个Excel文档里面所有的sheet，我们可以遍历它来定位想要读写的worksheet
target_sheet_title = 'regression'
target_sheet = None
for work_sheet in workbook.worksheets:
    print(work_sheet.title)
    if work_sheet.title == target_sheet_title:
        target_sheet = work_sheet
        break

if target_sheet:
    print("worksheet with title '{}' found".format(target_sheet_title))


#2.逐个遍历每个数据单元
for row_cells in target_sheet.rows:
    for row_cell in row_cells:
        print(row_cell.value)
    print()

