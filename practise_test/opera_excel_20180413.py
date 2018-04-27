#coding=utf-8
'''
文件名：opera_excel.py
作用：获取excel，并获取相关的sheets内容/行/单元格内容
作者：曾志坤，时间：20180326
'''
import xlrd
import os
from xlutils.copy import copy

class OperaExcl:
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

    def get_excel(self):
        '''
        获取excel
        :return: excel
        '''
        excel = xlrd.open_workbook(self.file_path)
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

    def get_cols(self):

        book = xlrd.open_workbook(self.file_path)
        sheet = book.sheet_by_name('Sheet1')
        col_num = sheet.ncols
        return col_num
    def get_cell(self,row,cell):
        '''
        获取单元格内容
        :param row:
        :param cell:
        :return:
        '''
        data = self.data.cell(row,cell)
        return data

    def write_value(self, i, row, column, value):
        '''
        把原来的excel值都copy下来，然后再在对应的sheet表里面传输值，write_save.write(i, row, 8, value):现在在第8列传入value值
        :param row:
        :param value:
        :return:
        '''
        read_value = self.excel
        write_data = copy(read_value)   #复制整个excel值
        write_save = write_data.get_sheet(0)      # sheet表从0开始算  保存到具体哪个sheet
        write_save.write(i, row, column, value)     #保存到具体哪一个单元格
        write_data.save(self.file_path)     #保存到具体的路径文件

    def gets_excel_value(self,casename):
        opera = OperaExcl()
        col_num = opera.get_cols()
        row = opera.get_lines()
        lists = []
        for i in range(1, row):
            #print(opera.get_cell(i,0).value)
            if opera.get_cell(i, 0).value == casename:
                for j in range(0, col_num):
                    lists.append(opera.get_cell(i, j).value)
                return lists
            else:
                continue


#实例化
if __name__ == '__main__':
    opera = OperaExcl()
    list=opera.gets_excel_value("test_05")
    print ("list:",list)
