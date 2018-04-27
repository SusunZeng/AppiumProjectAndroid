#coding=utf-8
'''
文件名：quitLogin_page.py
作用：取有关于查询转账页面所有元素信息
作者：曾志坤，时间：20180414

'''
from util.get_by_local import GetByLocal

class QueryTransferPage:
    # global driver
    # 获取登录退出页面所有的页面元素信息
    def __init__(self, driver):
        # base_driver = BaseDriver()
        # self.driver = base_driver.android_driver(driver)
        self.driver = driver
        self.get_by_local = GetByLocal(self.driver)
        # print('方法名QueryTransferPage：', driver)

    def get_action_list_element(self):
        '''
        获取移动银行主页面操作清单总选项元素信息
        :return:
        actionList = self.driver.find_element_by_id('com.gdnybank.m:id/recycler_shortcut')
        actionList.find_element_by_xpath('//*[contains(@text,"查询转账")]').click()
        '''
        return self.get_by_local.get_element('action_list','queryTransfer_element')
    def get_right_login_head_element(self):
        '''
        获取移动银行主页面右上角登录头像
        :return:
        '''
        return self.get_by_local.get_element('right_login_head','queryTransfer_element')
    def get_account_plaint_element(self):
        '''
        获取转账页面卡片右下角感叹号
        :return:
        '''
        return self.get_by_local.get_element('account_plaint','queryTransfer_element')

    def get_payee_message_element(self):
        '''
        获取转账页面的收款人信息
        :return:
        '''
        return self.get_by_local.get_element('payee_message','queryTransfer_element')
    def get_payee_name_element(self):
        '''
        获取收款人信息页面的账户姓名信息
        :return:
        '''
        return self.get_by_local.get_element('payee_name','queryTransfer_element')

    def get_payee_account_element(self):
        '''
        获取收款人信息页面的收款人账号信息
        :return:
        '''
        return self.get_by_local.get_element('payee_account','queryTransfer_element')

    def get_payee_input_element(self):
        '''
        获取收款人信息页面的有关于编辑框元素的元素
        :return:
        '''
        return self.get_by_local.get_element('payee_input_element','queryTransfer_element')

    def get_transfer_message_element(self):
        '''
        获取转账页面的转账金额/备注/手机短信三个元素
        :return:
        '''
        return self.get_by_local.get_element('transfer_message', 'queryTransfer_element')

    def get_transfer_tips_element(self):
        '''
        获取转账页面的确认转账信息
        :return:
        '''
        return self.get_by_local.get_element('transfer_tips','queryTransfer_element')

    def get_submit_transfer_element(self):
        '''
        获取转账页面的提交转账信息信息
        也是获取收款人信息页面的提交按钮信息
        :return:
        '''
        return self.get_by_local.get_element('submit_transfer','queryTransfer_element')

    def get_transfer_fast_element(self):
        '''
        获取收款人信息页面的快速转账方式信息
        :return:
        '''
        return self.get_by_local.get_element('transfer_fast','queryTransfer_element')

    def get_transfer_other_element(self):
        '''
        获取收款人信息页面的其他转账方式信息
        :return:
        '''
        return self.get_by_local.get_element('transfer_other','queryTransfer_element')

    def get_transfer_general_element(self):
        '''
        获取收款人信息页面的其他->普通转账方式信息
        :return:
        '''
        return self.get_by_local.get_element('transfer_general','queryTransfer_element')

    def get_transfer_tomorrow_element(self):
        '''
        获取收款人信息页面的其他->次日转账方式信息
        :return:
        '''
        return self.get_by_local.get_element('transfer_tomorrow','queryTransfer_element')

    def get_transfer_bank_name_element(self):
        '''
        获取收款人信息页面的银行名称信息
        :return:
        '''
        return self.get_by_local.get_element('transfer_bank_name','queryTransfer_element')

    def get_left_head_button_element(self):
        '''
        获取页面左上角的返回按钮信息
        :return:
        '''
        return self.get_by_local.get_element('left_head_button', 'queryTransfer_element')

    def get_search_bank_element(self):
        '''
        获取银行列表页面的搜索银行名称编辑框信息
        :return:
        '''
        return self.get_by_local.get_element('search_bank', 'queryTransfer_element')

    def get_search_button_element(self):
        '''
        获取银行列表页面的搜索按钮信息
        :return:
        '''
        return self.get_by_local.get_element('search_button', 'queryTransfer_element')

    def get_payee_list_edit_element(self):
        '''
        获取收款人列表页面的编辑按钮信息
        :return:
        '''
        return self.get_by_local.get_element('payee_list_edit', 'queryTransfer_element')

    def get_payee_delete_element(self):
        '''
        获取收款人列表页面的删除按钮信息
        :return:
        '''
        return self.get_by_local.get_element('payee_delete', 'queryTransfer_element')

    def get_payee_list_complete_element(self):
        '''
        获取收款人列表页面的完成按钮信息
        :return:
        '''
        return self.get_by_local.get_element('payee_list_complete', 'queryTransfer_element')

    def get_get_code_element(self):
        '''
        获取转账输入密码页面的获取验证码按钮信息
        :return:
        '''
        return self.get_by_local.get_element('get_code','queryTransfer_element')
    def get_input_code_element(self):
        '''
        获取转账输入密码页面的输入验证码编辑框信息
        :return:
        '''
        return self.get_by_local.get_element('input_code','queryTransfer_element')


    def get_draw_password_element(self):
        '''
        获取转账输入密码页面的输入取款密码编辑框信息
        :return:
        '''
        return self.get_by_local.get_element('draw_password','queryTransfer_element')

    def get_transfer_account_submit_element(self):
        '''
        获取转账输入密码页面的转账按钮信息
        :return:
        '''
        return self.get_by_local.get_element('transfer_account_submit','queryTransfer_element')

    def get_bank_list_element(self):
        '''
        获取银行列表页面的银行列表元素信息
        也是获取收款人清单元素信息
        :return:
        '''
        return self.get_by_local.get_element('bank_list','queryTransfer_element')

    def get_transfer_payee_head_element(self):
        '''
        获取收款人信息页面的账户姓名编辑框右侧的头像按钮元素信息
        :return:
        '''
        return self.get_by_local.get_element('transfer_payee_head','queryTransfer_element')

    def get_transfer_submitted_element(self):
        '''
        获取转账成功页面的“转账已提交”信息元素
        :return:
        '''
        return self.get_by_local.get_element('transfer_submitted','queryTransfer_element')

    def get_remaining_balance_element(self):
        '''
        获取转账成功页面的“余额”信息元素
        :return:
        '''
        return self.get_by_local.get_element('remaining_balance','queryTransfer_element')

    def get_inform_success_element(self):
        '''
        获取转账成功页面的“好，我知道了”通知成功按钮信息元素
        :return:
        '''
        return self.get_by_local.get_element('inform_success','queryTransfer_element')

    def get_transfer_again_element(self):
        '''
        获取转账成功页面的“再转一笔”按钮信息元素
        :return:
        '''
        return self.get_by_local.get_element('transfer_again', 'queryTransfer_element')

    def get_error_prompt_element(self):
        '''
        获取收款人页面提交的报错元素
        :return:
        '''
        return self.get_by_local.get_element('error_prompt', 'queryTransfer_element')

    def get_error_prompt_confirm_element(self):
        '''
        获取收款人页面提交的报错元素
        :return:
        '''
        return self.get_by_local.get_element('error_prompt_confirm', 'queryTransfer_element')

    def get_bank_list_card_element(self):
        '''
        获取收款人页面的收款人清单的银行卡号元素
        :return:
        '''
        return self.get_by_local.get_element('bank_list_card', 'queryTransfer_element')

    def get_search_bank_city_element(self):
        '''
        获取他行页面的搜索城市名称元素
        :return:
        '''
        return self.get_by_local.get_element('search_bank_city','queryTransfer_element')

    def get_branch_keyword_element(self):
        '''
        获取他行页面的“请输入支行关键字”元素
        :return:
        '''
        return self.get_by_local.get_element('branch_keyword','queryTransfer_element')

    def get_branch_search_element(self):
        '''
        获取他行页面的“搜索”按钮元素
        :return:
        '''
        return self.get_by_local.get_element('branch_search','queryTransfer_element')

    def get_search_city_element(self):
        '''
        获取他行页面->城市列表页面的“搜索城市名称”编辑框
        :return:
        '''
        return self.get_by_local.get_element('search_city','queryTransfer_element')

    def get_city_branch_search_element(self):
        '''
        获取他行页面->城市列表页面的“搜索”按钮
        :return:
        '''
        return self.get_by_local.get_element('city_branch_search','queryTransfer_element')

    def get_branch_bank_amount_element(self):
        '''
        获取他行页面的所有分行数量元素
        :return:
        '''
        return self.get_by_local.get_element('branch_bank_amount','queryTransfer_element')

    def get_city_list_element(self):
        '''
        获取城市列表页面的城市列表元素
        :return:
        actionList = self.driver.find_element_by_id('com.gdnybank.m:id/recycler_shortcut')
        actionList.find_element_by_xpath('//*[contains(@text,"查询转账")]').click()
        '''
        return self.get_by_local.get_element('city_list','queryTransfer_element')

    def get_title_head_element(self):
        '''
        获取城市列表页面的“城市列表标题”
        :return:
        '''
        return self.get_by_local.get_element('title_head','queryTransfer_element')

    def get_branch_bank_keyword_element(self):
        '''
        获取他行页面的查询支行关键查询列表元素
        :return:
        '''
        return self.get_by_local.get_element('branch_bank_keyword','queryTransfer_element')

    def get_account_types_element(self):
        '''
        获取账户详情页面的账户产品种类元素
        :return:
        '''
        return self.get_by_local.get_element('account_types','queryTransfer_element')

    def get_account_balance_element(self):
        '''
        获取账户详情页面的账户余额元素
        :return:
        '''
        return self.get_by_local.get_element('account_balance','queryTransfer_element')

    def get_regist_date_element(self):
        '''
        获取账户详情页面的开户日期元素
        :return:
        '''
        return self.get_by_local.get_element('regist_date','queryTransfer_element')

    def get_system_prompt_element(self):
        '''
        获取转账页面的报错弹框文本提示元素
        :return:
        '''
        return self.get_by_local.get_element('system_prompt','queryTransfer_element')

    def get_error_confirm_element(self):
        '''
        获取转账页面的报错弹框的按钮元素
        :return:
        '''
        return self.get_by_local.get_element('error_confirm','queryTransfer_element')

    def get_check_tran_tips_element(self):
        '''
        获取输入验证码和付款密码的转账页面温馨提示中，“我已确认继续完成本次交易！”按钮
        :return:
        '''
        return self.get_by_local.get_element('check_tran_tips','queryTransfer_element')

    def get_fail_title_element(self):
        '''
        获取输入超过6位密码时的报错元素
        :return:
        '''
        return self.get_by_local.get_element('fail_title','queryTransfer_element')

    def get_payee_list_name_element(self):
        '''
        获取收款人页面收款人列表元素
        :return:
        '''
        return self.get_by_local.get_element('payee_list_name','queryTransfer_element')
