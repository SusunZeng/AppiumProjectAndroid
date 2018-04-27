#coding=utf-8
'''
文件名：quitLogin_business.py
作用：查询转账业务流程，具体的业务流程按照手工测试来筛选
作者：曾志坤，时间：20180402
'''
from handle.queryTransfer_handle import QueryTransferHandle
from page.queryTransfer_page import QueryTransferPage
import time
from util.public_method import Public_Method
from util.read_excel import Read_Excel
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re

class MyAccount_Business:
    def __init__(self, driver):

        # base_driver = BaseDriver()
        # self.driver = base_driver.android_driver(driver)
        self.driver = driver
        self.queryTransfer_handle = QueryTransferHandle(self.driver)
        self.queryTransfer_page = QueryTransferPage(self.driver)
        self.public_method = Public_Method(self.driver)
        self.read_excel = Read_Excel('E:\\AppiumProjectAndroid\\config\\AppiumProjectData.xlsx', 'Sheet1')


    def hide_balance(self):
        action_list_element = self.driver.find_element_by_id('com.gdnybank.m:id/tv_fun_title')
        print('action_list_element：', action_list_element)
        print('单独功能：', action_list_element.get_attribute('text'))
        action_list_elements = self.driver.find_elements_by_id('com.gdnybank.m:id/tv_fun_title')
        print('action_list_elements:', action_list_elements)
        print('操作功能数量：', len(action_list_elements))
        print('操作哪个功能：', action_list_elements[9].get_attribute('text'))
        # action_list_element.find_element_by_xpath('//*[contains(@text,"我的账户")]').click()
        # action_list_elements.find_element_by_xpath('//*[contains(@text,"我的账户")]').click()
        action_list_elements[9].click()