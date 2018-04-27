#coding=utf-8
'''
文件名：login_handle.py
作用：操作登录页面的元素，在所有相关的元素均在该类LoginHandle维护
作者：曾志坤，时间：20180316
'''

from page.login_page import LoginPage
from util.pop_up_box import PopUpBox
import time

class LoginHandle:
    # global driver
    def __init__(self,i):
        self.login_page = LoginPage(i)
        self.driver = self.login_page.drivers()
        self.pop_up_box = PopUpBox()

    def drivers(self):
        return self.driver

    #操作登录页面的元素
    def send_username(self,user):
        '''
        输入用户名
        :param user:
        :return:
        '''
        self.login_page.get_username_element().clear()
        self.login_page.get_username_element().send_keys(user)

    def click_get_password(self):
        '''
        点击密码输入框，为能确保
        :return:
        '''
        self.login_page.get_password_element().click()

    def send_password(self,password):
        '''
        输入登录密码
        :param password:
        :return:
        '''
        self.login_page.get_password_element().send_keys(password)

    def clear_password(self):
        '''
        清空登录密码
        :return:
        '''
        self.login_page.get_password_element().clear()
    def click_login(self):
        '''
        点击登录按钮
        :return:
        '''
        self.login_page.get_login_button_element().click()

    def click_forget_password(self):
        '''
        点击忘记密码
        :return:
        '''
        self.login_page.get_forget_password_element().click()

    def click_register(self):
        '''
        点击注册手机银行
        :return:
        '''
        self.login_page.get_dredge_login_element().clcik()

    def get_fail_tost(self,message):
        '''
        获取tost，根据返回信息进行返回数据
        :param message:
        :return:
        '''
        tost_element = self.login_page.get_tost_element(message)
        print('tost_element:', tost_element)
        if tost_element:
            return True
        else:
            return False

    def send_verification_code(self):
        '''
        输入验证码
        :return:
        '''
        # root = App()
        # # root.master.title("验证码")
        # root.mainloop()
        # self.login_page.get_verification_code_element().click()
        # print('要素？',self.login_page.get_verification_code_element())

        # self.pop_up_box.PopUPFrame()
        code = self.pop_up_box.PopUPFrame()
        print('输入code:',code)
        self.login_page.get_verification_code_element().send_keys(code)


    def click_combobox(self):
        '''
        点击下拉框
        :return:
        '''
        self.login_page.get_combobox_element().click()

    def click_env_optionname(self,name):
        '''
        选择对应环境然后再点击
        :param name:
        :return:
        '''
        self.login_page.get_env_optionname_element(name).click()

    def click_env_confirm(self):
        '''
        选择测试环境后，点击确认进入下一步
        :return:
        '''
        self.login_page.get_env_confirm_element().click()

    def click_reservation_message(self):
        '''
        点击预留信息提示
        :return:
        '''
        self.login_page.get_reservation_message_element().click()

    def click_step_over(self):
        '''
        点击设置指纹跳过按钮，注意：若手机有指纹功能，则显示指纹设置；若没有，则显示手势设置
        :return:
        '''
        self.login_page.get_step_over_element().click()

    def click_system_prompt_button(self):
        '''
        点击系统提示框的确认按钮
        :return:
        '''
        self.login_page.get_system_prompt_button().click()

    def click_right_login_head_button(self):
        '''
        点击移动银行主页面右上角登录头像按钮
        :return:
        '''
        self.login_page.get_right_login_head_element().click()

    def click_left_head_button_button(self):
        '''
        点击页面左上角的返回按钮
        :return:
        '''
        self.login_page.get_left_head_button_element().click()

