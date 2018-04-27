#coding=utf-8
'''
文件名：login_business.py
作用：登录业务流程登录
作者：曾志坤，时间：20180316
'''
from handle.login_handle import LoginHandle
from page.login_page import LoginPage
import time
from util.public_method import Public_Method
# from util.pop_up_box import pop_up_box
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from util.read_excel import Read_Excel
from util.press_Keycode import Press_Keycode

class Login_Business:
    def __init__(self,i):

        self.login_handle = LoginHandle(i)
        self.driver = self.login_handle.drivers()
        self.public_method = Public_Method(self.driver)
        self.login_page = LoginPage(i)
        self.read_excel = Read_Excel('E:\\AppiumProjectAndroid\\config\\AppiumProjectData.xlsx','Sheet1')
        self.press_Keycode = Press_Keycode(self.driver)

    def drivers(self):
        return self.driver
    def login_before(self):

        self.login_handle.click_combobox()
        test_env = self.read_excel.get_cell(3, 2)
        if '外网测试环境' in test_env:
            self.public_method.swipe_on('up', 10000)
        combox_list = self.login_page.get_combox_list_element()
        combox_list.find_element_by_xpath(test_env).click()
        self.login_handle.click_env_confirm()
        time.sleep(8)

        keyword = '确认'
        confirm = '确认'
        while keyword in confirm:
            confirm = self.driver.find_element_by_class_name('android.widget.Button').get_attribute('text')
            # print('弹框信息关键词：', confirm)
            # if keyword in confirm:
            self.driver.find_element_by_class_name('android.widget.Button').click()



    def login_pass(self):
        '''
        登录成功
        :return:
        '''
        # 点击右上角的人头进行登录
        self.login_handle.click_right_login_head_button()
        username_pass = self.read_excel.get_cell(3, 5)
        password_pass = self.read_excel.get_cell(3, 6)
        print('账号密码：',username_pass,',',password_pass)

        self.login_handle.send_username(username_pass)  # 验证输入账号
        self.login_handle.click_get_password()
        self.login_handle.clear_password()
        self.login_handle.send_password(password_pass)
        # 弹出框输入验证码
        self.login_handle.send_verification_code()
        time.sleep(5)
        self.login_handle.click_login()
        time.sleep(15)

        self.login_handle.click_reservation_message()
        self.login_handle.click_step_over()

        keyword = '确认'
        confirm = '确认'
        while keyword in confirm:
            confirm = self.driver.find_element_by_class_name('android.widget.Button').get_attribute('text')
            # print('弹框信息关键词：', confirm)
            # if keyword in confirm:
            self.driver.find_element_by_class_name('android.widget.Button').click()

    def login_user_error(self):
        '''
        用户名输入错误报错，待定
        :return:
        '''
        # self.login_handle.click_right_login_head_button()
        # 点击右上角的人头进行登录
        self.login_handle.click_right_login_head_button()
        username_error = self.read_excel.get_cell(2, 5)
        password_error = self.read_excel.get_cell(2, 6)
        print('账号密码：',username_error,',',password_error)
        self.login_handle.send_username(username_error)
        self.login_handle.click_get_password()
        self.login_handle.clear_password()
        self.login_handle.send_password(password_error)
        # 弹出框输入验证码
        self.login_handle.send_verification_code()
        time.sleep(5)
        self.login_handle.click_login()

        user_flag= self.login_handle.get_fail_tost('登录名格式不正确')
        print('user_flag:',user_flag)
        self.login_handle.click_system_prompt_button()
        self.login_handle.click_left_head_button_button()
        # self.opera_excel().write_value(21,user_flag)
        if user_flag:
            return True
        else:
            return False


# if __name__ == '__main__':
#     loginBusiness = LoginBusiness(0)
#     loginpass = loginBusiness.login_pass()
#     print(loginpass)