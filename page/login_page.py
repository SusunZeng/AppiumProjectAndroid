#coding=utf-8
'''
文件名：LoginPage.py
作用：取登录页面所有元素信息
作者：曾志坤，时间：20180316

'''
from util.get_by_local import GetByLocal
import time
from base.base_driver import BaseDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    # global driver
    # 获取登录页面所有的页面元素信息
    def __init__(self,driver):
        # base_driver = BaseDriver()
        # self.driver = base_driver.android_driver(i)
        self.driver = driver
        self.get_by_local = GetByLocal(self.driver)

        # driver = self.driver
    def drivers(self):
        return self.driver

    def get_username_element(self):
        '''
        获取用户名元素信息
        '''
        return self.get_by_local.get_element('username','login_element')

    def get_password_element(self):
        '''
        获取密码元素信息
        '''
        return self.get_by_local.get_element('password','login_element')

    def get_verification_code_element(self):
        '''
        获取验证码元素信息，注意取的是classname，elements[2]
        '''
        return self.get_by_local.get_element('verification_code','login_element')


    def get_code_retry_element(self):
        '''
        获取验证码点击重试元素信息
        '''
        return self.get_by_local.get_element('code_retry','login_element')


    def get_remember_login_element(self):
        '''
        获取记住登录名元素信息
        '''
        return self.get_by_local.get_element('remember_login','login_element')


    def get_forget_password_element(self):
        '''
        获取忘记密码元素信息
        '''
        return self.get_by_local.get_element('forget_password','login_element')

    def get_login_button_element(self):
        '''
        获取登录元素信息
        '''
        return self.get_by_local.get_element('login_button','login_element')

    def get_dredge_login_element(self):
        '''
        获取注册手机银行元素信息
        '''
        return self.get_by_local.get_element('dredge_login','login_element')

    def get_register_direct_bank_element(self):
        '''
        获取开立电子账户并注册手机银行元素信息
        '''
        return self.get_by_local.get_element('register_direct_bank','login_element')

    def get_tost_element(self,message):
        '''
        获取账户错误元素信息，待定
        '''
        time.sleep(2)
        tost_element = ("xpath", "//*[contains(@text," + message + ")]")
        return WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located(tost_element))

    '''
    获取密码输入错误元素信息，待定
    '''

    '''
    获取验证码输入错误元素信息，待定
    '''
    def get_system_prompt_button(self):
        '''
        获取系统提示框元素信息
        :param message:
        :return:
        '''

        return self.get_by_local.get_element('system_prompt_button','login_element')

    def get_combobox_element(self):
        '''
        获取下拉框元素信息
        :return:
        '''
        return self.get_by_local.get_element('combobox','login_element')

    def get_env_optionname_element(self,name):
        '''
        获取下拉框选项信息
        :param name:
        :return:
        '''
        env_optionname = ('text(\"'+name+'\")')
        return self.get_by_local.get_element(env_optionname,'login_element')
        # find_element_by_android_uiautomator('text(\"' + name + '\")')

    def get_env_confirm_element(self):
        '''
        获取环境选择的确认信息
        :return:
        '''
        return self.get_by_local.get_element('env_confirm','login_element')

    def get_reservation_message_element(self):
        '''
        获取登录成功后的预留信息
        :return:
        '''
        return self.get_by_local.get_element('reservation_message','login_element')

    def get_step_over_element(self):
        '''
        获取设置指纹登录跳过按钮
        :return:
        '''
        return self.get_by_local.get_element('step_over','login_element')

    def get_right_login_head_element(self):
        '''
        获取移动银行主页面右上角登录头像
        :return:
        '''
        return self.get_by_local.get_element('right_login_head','login_element')

    def get_combox_list_element(self):
        '''
        获取测试环境的下拉框元素
        :return:
        '''
        return self.get_by_local.get_element('combox_list','login_element')

    def get_left_head_button_element(self):
        '''
        获取页面左上角的返回按钮信息
        :return:
        '''
        return self.get_by_local.get_element('left_head_button', 'login_element')
