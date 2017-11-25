
from openpyxl import Workbook

wb=Workbook()

ws=wb.active

ws['A1']="This is a test"

wb.save('test.xlsx')


