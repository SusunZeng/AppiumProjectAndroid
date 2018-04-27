#
# import sys
# sys.path.append("E:\\AppiumProjectAndroid\\config")
# import openpyxl
#
# #新建excel
# def creatwb(wbname):
#     wb=openpyxl.Workbook()
#     wb.save(filename=wbname)
#     print ("新建Excel："+wbname+"成功")
#
# # 写入excel文件中 date 数据， fields 表头
# def savetoexcel(data,fields,sheetname,wbname):
#     print("写入excel：")
#     wb=openpyxl.load_workbook(filename=wbname)
#
#     sheet=wb.active
#     sheet.title=sheetname
#
#     field=1
#     for field in range(1,len(fields)+1):   # 写入表头
#         _=sheet.cell(row=1,column=field,value=str(fields[field-1]))
#
#     row1=1
#     col1=0
#     for row1 in range(2,len(data)+2):  # 写入数据
#         for col1 in range(1,len(data[row1-2])+1):
#             _=sheet.cell(row=row1,column=col1,value=str(data[row1-2][col1-1]))
#
#     wb.save(filename=wbname)
#     print("保存成功")
#
# creatwb('AndroidAutomationTestCase-3')
# savetoexcel('123','2','Sheet1','AndroidAutomationTestCase-3')




# from openpyxl import Workbook
# wb = Workbook()
#
# # grab the active worksheet
# ws = wb.active
#
# # Data can be assigned directly to cells
# ws['A1'] = 42
#
# # Rows can also be appended
# ws.append([1, 2, 3])
#
# # Python types will automatically be converted
# import datetime
# ws['A2'] = datetime.datetime.now()
#
# # Save the file
# # file_path='E:\\AppiumProjectAndroid\\config\\AndroidAutomationTestCase-1.xls'
# wb.save("E:\\AppiumProjectAndroid\\config\\sample.xlsx")

#coding=utf-8
import xlsxwriter
def add_excel():

    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook('E:\\AppiumProjectAndroid\\config\\ABC.xls')
    worksheet = workbook.add_worksheet()

    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': True})

    # Add a number format for cells with money.
    money = workbook.add_format({'num_format': '$#,##0'})

    # Write some data headers.
    worksheet.write('A1', 'Item', bold)
    worksheet.write('B1', 'Cost', bold)

    # Some data we want to write to the worksheet.
    expenses = (
     ['Rent', 1000],
     ['Gas',   100],
     ['Food',  300],
     ['Gym',    50],
    )

    # Start from the first cell below the headers.
    row = 1
    col = 0

    # Iterate over the data and write it out row by row.
    for item, cost in (expenses):
     worksheet.write(row, col,     item)
     worksheet.write(row, col + 1, cost, money)
     row += 1

    # Write a total using a formula.
    worksheet.write(row, 0, 'Total',       bold)
    worksheet.write(row, 1, '=SUM(B2:B5)', money)

    workbook.close()

add_excel()