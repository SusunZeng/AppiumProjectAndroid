#coding=utf-8
'''
文件名：quitLogin_handle.py
作用：操作登录退出页面所有元素信息
作者：曾志坤，时间：20180402

'''
from page.quitLogin_page import QuitLoginPage

class QuitLoginHandle:

    def __init__(self, driver):
        # base_driver = BaseDriver()
        # self.driver = base_driver.android_driver(driver)
        self.driver = driver
        self.quitLogin_page = QuitLoginPage(self.driver)
        # print('方法名QuitLoginHandle：', driver)

    def click_left_button(self):
        '''
        点击左上角按钮
        :return:
        '''
        self.quitLogin_page.get_left_button_element().click()

    def click_exit_button(self):
        '''
        点击安全退出按钮
        :return:
        '''
        self.quitLogin_page.get_exit_button_element().click()

    def click_confirm_exit(self):
        '''
        点击确认退出按钮
        :return:
        '''
        self.quitLogin_page.get_confirm_exit_element().click()


