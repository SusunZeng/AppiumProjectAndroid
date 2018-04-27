#coding=utf-8
'''
文件名：quitLogin_handle.py
作用：操作查询转账页面所有元素信息
作者：曾志坤，时间：20180414

'''
from page.queryTransfer_page import QueryTransferPage
from util.pop_up_box import PopUpBox
import time

class QueryTransferHandle:

    def __init__(self, driver):
        # base_driver = BaseDriver()
        # self.driver = base_driver.android_driver(driver)
        self.driver = driver
        self.queryTransfer_page = QueryTransferPage(self.driver)
        self.pop_up_box = PopUpBox()
        # print('方法名QueryTransferHandle：', driver)

    def click_action_list_button(self ,xpathAddress):
        '''
        继续获取移动银行主页面操作清单的xpath清单元素
        :param xpathAddress:
        :return:
        actionList = self.driver.find_element_by_id('com.gdnybank.m:id/recycler_shortcut')
        actionList.find_element_by_xpath('//*[contains(@text,"查询转账")]').click()
        '''
        self.queryTransfer_page.get_action_list_element().find_element_by_xpath(xpathAddress).click()
    def click_right_login_head_button(self):
        '''
        点击移动银行主页面右上角登录头像按钮
        :return:
        '''
        self.queryTransfer_page.get_right_login_head_element().click()
    def click_account_plaint_button(self):
        '''
        点击转账页面卡片右下角感叹号
        :return:
        '''
        self.queryTransfer_page.get_account_plaint_element().click()
        time.sleep(2)

    # def send_payee_name_code(self,payeeName):
    #     '''
    #     输入转账页面的收款人信息
    #     :param payeeName:
    #     :return:
    #     '''
    #     self.queryTransfer_page.get_payee_name_element().send_keys(payeeName)

    def click_payee_message_button(self):
        '''
        点击转账页面的收款人按钮
        :param payeeName:
        :return:
        '''
        self.queryTransfer_page.get_payee_message_element().click()

    def send_payee_name_code(self ,payeeName):
        '''
        输入收款人信息页面的账户姓名信息
        :param payeeName:
        :return:
        '''
        time.sleep(2)
        self.queryTransfer_page.get_payee_name_element().send_keys(payeeName)

    def send_payee_account_code(self ,payeeAccount):
        '''
        输入收款人信息页面的收款人账号信息
        :param payeeName:
        :return:
        '''
        time.sleep(2)
        # print('收款人账号元素：', self.queryTransfer_page.get_payee_account_element())
        self.queryTransfer_page.get_payee_account_element().click()
        time.sleep(10)
        self.queryTransfer_page.get_payee_account_element().send_keys(payeeAccount)
        time.sleep(2)
    def clear_payee_account_code(self):
        '''
        清除收款人信息页面的收款人账号信息
        :return:
        '''
        self.queryTransfer_page.get_payee_account_element().clear()

    def get_payee_account_code(self):
        '''
        获取收款人信息页面的收款人账号信息text
        :return:
        payee_account_after = self.driver.find_elements_by_id('com.gdnybank.m:id/m_combin_edit')[1].get_attribute(
                "text")
        '''
        time.sleep(5)
        self.queryTransfer_page.get_payee_account_element().get_attribute("text")

    def send_transfer_amount_code(self ,transferAmount):
        '''
        输入转账页面的转账金额(人民币)
        :param payeeName:
        :return:
        '''
        self.queryTransfer_page.get_transfer_message_element()[0].send_keys(transferAmount)

    def click_transfer_tips_head_button(self):
        '''
        点击移动银行主页面确认转账金额、用途及收款方按钮
        :return:
        '''
        self.queryTransfer_page.get_transfer_tips_element().click()

    def click_submit_transfer_button(self):
        '''
        点击移动银行主页面提交转账信息按钮
        也是点击收款人信息页面的提交按钮
        :return:
        '''
        self.queryTransfer_page.get_submit_transfer_element().click()
        time.sleep(2)


    def click_transfer_fast_button(self):
        '''
        点击收款人信息页面的快速转账方式按钮
        :return:
        '''
        self.queryTransfer_page.get_transfer_fast_element().click()

    def click_transfer_other_button(self):
        '''
        点击收款人信息页面的其他转账方式按钮
        :return:
        '''
        self.queryTransfer_page.get_transfer_other_element().click()

    def click_transfer_general_button(self):
        '''
        点击收款人信息页面的其他->普通转账方式按钮
        :return:
        '''
        self.queryTransfer_page.get_transfer_general_element().click()

    def click_transfer_tomorrow_button(self):
        '''
        点击收款人信息页面的其他->次日转账方式按钮
        :return:
        '''
        self.queryTransfer_page.get_transfer_tomorrow_element().click()

    def click_transfer_bank_name_button(self):
        '''
        点击收款人信息页面的银行名称按钮
        :return:
        '''
        self.queryTransfer_page.get_transfer_bank_name_element().click()


    def click_left_head_button_button(self):
        '''
        点击页面左上角的返回按钮
        :return:
        '''
        self.queryTransfer_page.get_left_head_button_element().click()

    def send_search_bank_code(self ,searchBankName):
        '''
        在银行列表页面输入搜索银行名称
        :param searchBankName:
        :return:
        '''
        self.queryTransfer_page.get_search_bank_element().send_keys(searchBankName)

    def click_search_button_button(self):
        '''
        点击银行列表页面的搜索按钮
        :return:
        '''
        self.queryTransfer_page.get_search_button_element().click()
        time.sleep(2)

    def click_payee_list_edit_button(self):
        '''
        点击收款人列表页面的编辑按钮
        :return:
        '''
        self.queryTransfer_page.get_payee_list_edit_element().click()

    def click_payee_delete_button(self):
        '''
        点击收款人列表页面的删除按钮
        :return:
        '''
        self.queryTransfer_page.get_payee_list_edit_element().click()

    def click_payee_list_complete_button(self):
        '''
        点击收款人列表页面的完成按钮
        :return:
        '''
        self.queryTransfer_page.get_payee_list_complete_element().click()

    def click_get_code_button(self):
        '''
        点击转账输入密码页面的获取验证码按钮
        :return:
        '''
        time.sleep(3)
        self.queryTransfer_page.get_get_code_element().click()
        time.sleep(2)

    def send_input_code_code(self):
        '''
        在转账输入密码页面的输入验证码信息
        :return:
        '''
        time.sleep(5)
        drawCode = self.pop_up_box.PopUPFrame()
        print('输入code:' ,drawCode)
        self.queryTransfer_page.get_input_code_element().send_keys(drawCode)

    def click_input_code_code(self):
        '''
        在转账输入密码页面再次点击验证码编辑框
        :return:
        '''
        self.queryTransfer_page.get_input_code_element().click()

    def send_draw_password_code(self ,drawPassword):
        '''
        在转账输入密码页面的输入密码信息
        :return:
        '''
        time.sleep(2)
        self.queryTransfer_page.get_draw_password_element().send_keys(drawPassword)

    def click_draw_password_button(self):
        '''
        点击转账输入密码页面的输入密码按钮
        :return:
        '''
        self.queryTransfer_page.get_draw_password_element().click()

    def click_transfer_account_submit_button(self):
        '''
        点击转账输入密码页面的转账按钮
        :return:
        '''
        self.queryTransfer_page.get_transfer_account_submit_element().click()
        time.sleep(8)

    def click_bank_list_list(self ,xpathAddress):
        '''
        点击银行列表页面的银行列表xpath清单元素
        也是选择点击收款人列表的xpath元素
        :param xpathAddress:
        :return:
        self.driver.find_element_by_id('com.gdnybank.m:id/lv_bank_list').\
            find_element_by_xpath('//*[contains(@text,"广东南粤银行")]').click()
        '''
        self.queryTransfer_page.get_bank_list_element().find_element_by_xpath(xpathAddress).click()
        time.sleep(2)

    def click_transfer_payee_head_button(self):
        '''
        点击收款人信息页面的账户姓名编辑框右侧的头像按钮
        :return:
        '''
        self.queryTransfer_page.get_transfer_payee_head_element().click()
        time.sleep(3)

    def get_transfer_submitted_text(self):
        '''
        获取转账成功页面的“转账已提交”元素属性值
        :return:
        '''
        self.queryTransfer_page.get_transfer_submitted_element().get_attribute("text")

    def get_remaining_balance_text(self):
        '''
        获取转账成功页面的“余额”元素属性值
        :return:
        '''
        self.queryTransfer_page.get_remaining_balance_element().get_attribute('text')

    def click_inform_success_button(self):
        '''
        点击转账成功页面的“好，我知道了”通知成功按钮
        :return:
        '''
        self.queryTransfer_page.get_inform_success_element().click()

    def click_transfer_again_button(self):
        '''
        点击转账成功页面的“再转一笔”按钮
        :return:
        '''
        self.queryTransfer_page.get_transfer_again_element().click()

    def get_error_prompt_value(self, property_value):
        '''
        获取收款人页面提交的报错的值
        :return:
        '''
        self.queryTransfer_page.get_error_prompt_element().get_attribute(property_value)

    def click_error_prompt_confirm_button(self):
        '''
        点击收款人页面提交的报错按钮
        :return:
        '''
        self.queryTransfer_page.get_error_prompt_confirm_element().click()

    def click_search_city_button(self):
        '''
        点击他行页面的搜索城市名称编辑框
        :return:
        '''
        self.queryTransfer_page.get_search_bank_city_element().click()

    def send_branch_keyword_code(self,branchKeyword):
        '''
        在他行页面的输入城市支行关键字
        :param branchKeyword:
        :return:
        '''
        self.queryTransfer_page.get_branch_keyword_element().send_keys(branchKeyword)

    def click_branch_search_button(self):
        '''
        点击他行页面的搜索按钮
        :param branchKeyword:
        :return:
        '''
        self.queryTransfer_page.get_branch_search_element().click()
        time.sleep(3)

    def send_search_city_code(self,cityName):
        '''
        在他行页面->城市列表页面的“搜索城市名称”编辑框输入值
        :param cityName:
        :return:
        '''
        self.queryTransfer_page.get_search_city_element().send_keys(cityName)

    def click_city_branch_search_button(self):
        '''
        点击他行页面->城市列表页面的“搜索”按钮
        :return:
        '''
        self.queryTransfer_page.get_city_branch_search_element().click()
        time.sleep(2)

    def click_check_tran_tips_button(self):
        '''
        点击输入验证码和付款密码的转账页面温馨提示中，“我已确认继续完成本次交易！”按钮
        :return:
        '''
        self.queryTransfer_page.get_check_tran_tips_element().click()

