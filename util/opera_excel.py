#coding=utf-8
'''
文件名：opera_excel.py
作用：获取excel，并获取相关的sheets内容/行/单元格内容
作者：曾志坤，时间：20180326
'''
import xlrd
from xlutils.copy import copy
import xlsxwriter
# import time

class OperaExcel:
    def __init__(self,file_path=None,i=None):
        '''
        构造函数
        :param file_path:
        '''
        if file_path == None:
            self.file_path = 'E:\\AppiumProjectAndroid\\config\\AndroidAutomationTestCase.xls'
        else:
            self.file_path = file_path
        if i == None:
            i = 0

        self.excel = self.get_excel()
        self.data = self.get_sheets(i)
        self.workbook = xlsxwriter.Workbook(self.file_path)

    def get_excel(self):
        '''
        获取excel
        :return: excel
        formatting_info=True
        '''
        excel = xlrd.open_workbook(self.file_path, formatting_info=True)
        return excel

    def get_sheets(self,i):
        '''
        获取sheets的内容
        :param i:
        :return:
        '''
        tables = self.excel.sheets()[i]
        return tables

    def get_lines(self):
        '''
        获取excel行数
        :return: lines
        '''
        lines = self.data.nrows
        return lines

    def get_cols(self, sheetName):
        '''
        获取excel列数的最大值
        :return: col_num
        作者：庄高，时间：201804
        '''
        # book = xlrd.open_workbook(self.file_path)
        # sheet = book.sheet_by_name('Sheet1')
        sheet = self.excel.sheet_by_name(sheetName) #根据已有的参数来修改，sheet值按照所传入的sheetName来取
        col_num = sheet.ncols
        return col_num

    def get_cell(self,row,column):
        '''
        获取单元格内容
        :param row:
        :param cell:
        :return: data
        '''
        data = self.data.cell(row,column).value
        return data

    def write_value(self, row, column, value):
        '''
        把原来的excel值都copy下来，然后再在对应的sheet表里面传输值，write_save.write(i, row, 8, value):现在在第8列传入value值
        :param row:
        :param value:
        :return:
        '''
        read_value = self.excel
        print('read_value:', read_value)
        write_data = copy(read_value)   #复制整个excel值
        print('write_data:', write_data)
        write_save = write_data.get_sheet(0)      # sheet表从0开始算  保存到具体哪个sheet
        print('copy的sheet值：',write_save)
        f = write_save.write(row, column, value)     #保存到具体哪一个单元格
        print('保存：', f)
        write_data.save(self.file_path)     #保存到具体的路径文件
        self.workbook.close()

    def gets_excel_value(self,sheetName,casename):

        # opera = OperaExcl()
        # col_num = opera.get_cols(sheetName)
        col_num = self.get_cols(sheetName)
        # row = opera.get_lines()
        row = self.get_lines()
        lists = []
        for i in range(1, row):
            # print(self.get_cell(i,0).value)
            if self.get_cell(i, 0).value == casename:
                for j in range(0, col_num):
                    lists.append(self.get_cell(i, j).value)
                return lists
            else:
                continue

#实例化
if __name__ == '__main__':
    opera = OperaExcel()
    print(opera)
    # print('excel：', opera.get_excel())
    # print('sheet:', opera.get_sheets(0),opera.get_sheets(1))
    # print('lines:', opera.get_lines())
    # print("单元格的值：",opera.get_cell(1,2).value)
    # print('转账金额：',opera.get_cell(6, 10).value)
    opera.write_value(22,10, 'nice123')
    # time.sleep(5)
    print('输入一：', opera.get_cell(22, 10).value)
    # time.sleep(5)
    print("单元格的值：", opera.get_cell(5, 2).value)
    opera.write_value(23, 9, '通过')
    # time.sleep(5)
    print('输入二：', opera.get_cell(23, 9).value)
    # time.sleep(5)
    print('lines:', opera.get_lines())
    opera.write_value(22, 9, '失败123')
    # time.sleep(5)
    print('输入三：', opera.get_cell(22, 9).value)
    # print(opera.get_cell(4, 3).value)
    # list=opera.gets_excel_value('Sheet1',"test_1")
    # print ("list:",list[1])


