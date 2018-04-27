#coding=utf-8
'''
文件名：quitLogin_business.py
作用：登录退出业务流程
作者：曾志坤，时间：20180402
'''
from handle.quitLogin_handle import QuitLoginHandle
from base.driver_init import DriverInit

class QuitLogin_Business:
    def __init__(self,driver):

        # base_driver = BaseDriver()
        # self.driver = base_driver.android_driver(driver)
        self.driver = driver
        self.quitLoginHandle = QuitLoginHandle(self.driver)
        # print('方法名QuitLoginBusiness：', driver)

    def quitLogin_pass(self):
        # print('开始做登陆流程以外操作？')

        self.quitLoginHandle.click_left_button()
        self.quitLoginHandle.click_exit_button()
        self.quitLoginHandle.click_confirm_exit()
        # 如果存在最新公告信息，则判断点击确认
        for i in range(2):
            keyword = '确认'
            confirm = self.driver.find_element_by_class_name('android.widget.Button').get_attribute('text')
            # print('弹框信息关键词：', confirm)
            if keyword in confirm:
                self.driver.find_element_by_class_name('android.widget.Button').click()

# if __name__ == '__main__':
#     quitLogin_business = QuitLoginBusiness()
#     quitLogin_business.driver_call()

