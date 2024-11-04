#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : qiang.hu
# @Time: 2024/10/26

from openpyxl import load_workbook

excel_file = 'tests.xlsx'
workbook = load_workbook(filename=excel_file)

target_sheets=[work_sheet for work_sheet in workbook.worksheets  if work_sheet.title == 'regression']
target_sheet=target_sheets[0]
print(target_sheet.title)

for row_cells in target_sheet.rows:
    if row_cells[0].row == 1:
        continue
    row_cells[-1].value = 'unassigned'

for row_cells in target_sheet.rows:
    for cell in row_cells:
        print(cell.value)
    print()
workbook.save(filename=excel_file)
