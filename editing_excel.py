import openpyxl
import os

wb = openpyxl.Workbook()

print(wb.get_sheet_names())

sheet = wb.get_sheet_by_name('Sheet')

sheet['A1'] = 42
sheet['A2'] = 'hello'

wb.save('example.xlsx')