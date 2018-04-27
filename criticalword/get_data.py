#coding=utf-8
'''
文件名：get_data.py
作用：获取excel相应的值，其中，如self.opera_excel.get_cell(row,3)的“3”为固定值，具体可对应到excel查看，从0开始算
作者：曾志坤，时间：20180326
'''
from util.opera_excel import OperaExcel
class GetData:
    # 构造方法
    def __init__(self):
        self.opera_excel = OperaExcel()

    # 重新导入case，使用该函数
    def get_case_lines(self):
        '''
        获取case的行数
        :return: lines
        '''
        lines = self.opera_excel.get_lines()
        return lines

    def get_handle_step(self,row):
        '''
        获取操作步骤里面的操作方法名字
        :param row:
        :return:
        '''
        method_name = self.opera_excel.get_cell(row,3)
        return method_name

    def get_element_key(self,row):
        '''
        获取操作元素的key，元素的值为空时，需要返回None
        :param row:
        :return: element_key
        '''
        element_key = self.opera_excel.get_cell(row,4)
        if element_key == '':
            return None         #在python2 没有添加这一判断，则会报错，在python3，加不加这判断，都是直接返回空值
        return element_key

    def get_handle_value(self,row):
        '''
        获取操作元素的值
        :param row:
        :return:
        '''
        handle_value = self.opera_excel.get_cell(row,5)
        if handle_value == '':
            return None
        return handle_value

    def get_expect_element(self,row):
        '''
        获取预期结果元素element
        :param row:
        :return:
        '''
        expect_element = self.opera_excel.get_cell(row,6)
        if expect_element == '':
            return None
        return expect_element
    def get_is_run(self,row):
        '''
        获取是否运行
        :param row:
        :return:
        '''
        is_run = self.opera_excel.get_cell(row,8)
        if is_run == 'yes':
            return True
        else:
            return False

    def get_expect_handle(self,row):
        '''
        获取预期步骤值
        :param row:
        :return:
        '''
        expect_step = self.opera_excel.get_cell(row,7)
        if expect_step == '':
            return None
        return expect_step

    def write_value(self,row,column,value):
        '''
        在确定的cell单元格内传输参数
        :param row:
        :param column:
        :param value:
        :return:
        '''
        self.opera_excel.write_value(row,column,value)

    def get_cell_value(self,row,column):

        cell_value = self.opera_excel.get_cell(row,column).value
        if cell_value == '':
            return None         #在python2 没有添加这一判断，则会报错，在python3，加不加这判断，都是直接返回空值
        return cell_value



if __name__ == '__main__':
    get = GetData()
    print(get.get_element_key(13))
    print(get.write_value(103,2,'pass'))
    print('单元格：',get.get_cell_value(103,2))


