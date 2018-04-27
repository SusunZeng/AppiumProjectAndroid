#coding=utf-8
'''
文件名：quitLogin_page.py
作用：取登录退出页面所有元素信息
作者：曾志坤，时间：20180402

'''
from util.get_by_local import GetByLocal

class QuitLoginPage:
    # global driver
    # 获取登录退出页面所有的页面元素信息
    def __init__(self, driver):
        # base_driver = BaseDriver()
        # self.driver = base_driver.android_driver(driver)
        self.driver = driver
        self.get_by_local = GetByLocal(self.driver)
        # print('方法名QuitLoginPage：', driver)

    def get_left_button_element(self):
        '''
        获取左上角退出按钮元素
        :return:
        '''
        print('button_element:',self.get_by_local.get_element('left_button','quitLogin_element'))
        return self.get_by_local.get_element('left_button','quitLogin_element')

    def get_exit_button_element(self):
        '''
        获取安全退出按钮元素
        :return:
        '''
        return self.get_by_local.get_element('exit_button','quitLogin_element')

    def get_confirm_exit_element(self):
        '''
        获取确认退出元素
        :return:
        '''
        return self.get_by_local.get_element('confirm_exit','quitLogin_element')
