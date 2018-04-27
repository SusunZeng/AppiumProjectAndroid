#coding=utf-8
'''
文件名：quitLogin_handle.py
作用：操作关于我的账户，即是账户详情页面所有元素按钮
作者：曾志坤，时间：20180418

'''
from page.myAccount_page import MyAccountPage
from util.pop_up_box import PopUpBox
import time

class QueryTransferHandle:

    def __init__(self, driver):
        # base_driver = BaseDriver()
        # self.driver = base_driver.android_driver(driver)
        self.driver = driver
        self.myAccount_page = MyAccountPage(self.driver)
        self.pop_up_box = PopUpBox()
        # print('方法名QueryTransferHandle：', driver)

    def click_action_list_button(self,actionNum):
        '''
        选择对应的功能选项，其中actionNum功能选项选择的第几位，其中从左往右数，再往下数来排第几位，比如“我的账户”是第9位，‘明细查询’是第3位
        :param actionNum:
        :return:
        '''
        self.myAccount_page.get_action_list_element()[actionNum].click()
        time.sleep(3)
