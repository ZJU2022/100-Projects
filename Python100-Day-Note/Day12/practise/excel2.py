"""
创建Excel文件
"""
from openpyxl import Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo

workbook = Workbook()
worksheet = workbook.active
data = [[1001,'白元芳','男','1714005413'],[1002,'白洁','女','15680767295']]
worksheet.append(['学号','姓名','性别','联系方式'])
for row in data:
    worksheet.append(row)
tab = Table(displayName='Table1',ref='A1:E5')
tab.tableStyleInfo = TableStyleInfo(
    name="TableStyleMedium9", showFirstColumn=False,
    showLastColumn=False, showRowStripes=True, showColumnStripes=True)
#worksheet.add_table(tab)
workbook.save('./res/全班学生数据2.xlsx')