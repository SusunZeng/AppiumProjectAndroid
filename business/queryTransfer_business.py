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
from util.write_excel import Write_Excel
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re
from util.press_Keycode import Press_Keycode

class QueryTransfer_Business:
    def __init__(self, driver):
        self.driver = driver
        self.queryTransfer_handle = QueryTransferHandle(self.driver)
        self.queryTransfer_page = QueryTransferPage(self.driver)
        self.public_method = Public_Method(self.driver)
        self.read_excel = Read_Excel('E:\\AppiumProjectAndroid\\config\\AppiumProjectData.xlsx', 'Sheet1')
        self.write_excel = Write_Excel('E:\\AppiumProjectAndroid\\config\\AppiumProjectData.xlsx')
        self.press_Keycode = Press_Keycode(self.driver)

    #--------------------------------------------查询转账->快速转账------------------------------------------------------
    '''
    查询转账->快速转账
    '''
    def query_transferF_input(self):
        '''
        用例编号：111CZSX022,所有功能-查询转账-快速转账
        同行转账-正确输入金额-》步骤：进入快速转账，输入收款人姓名、账号，在银行列表选择同行进行转账，转账金额在（0，余额]之内
        query_transfer_input：输入收款人信息来快速转账
        :return:
        '''
        # 选择操作清单
        self.queryTransfer_handle.click_action_list_button('//*[contains(@text,"查询转账")]')
        self.queryTransfer_handle.click_payee_message_button()
        self.queryTransfer_handle.click_transfer_fast_button()
        payee_name = self.read_excel.get_cell(4, 8)
        print('payee_name:',payee_name)
        self.queryTransfer_handle.send_payee_name_code(payee_name)

        # 判断当所输入账号与预期的不一致时，则输入，否则继续下一步选择银行名称
        payee_account = self.read_excel.get_cell(4, 9)
        print('payee_account:', payee_account)
        payee_account_after = 1
        while payee_account != payee_account_after:
            # payee_account = '6235 9574 0000 6141 031'
            # 清除
            self.queryTransfer_handle.clear_payee_account_code()
            time.sleep(5)
            # 输入银行账号
            input_element = self.queryTransfer_page.get_payee_account_element()
            input_element.click()
            self.press_Keycode.press_Keycode(payee_account, input_element)

            # self.queryTransfer_handle.send_payee_account_code(payee_account)
            # 获取输入后的银行账号
            time.sleep(2)

            payee_account_after_original = self.queryTransfer_page.get_payee_input_element()[1].get_attribute("text")
            # print('payee_account_after_original:', payee_account_after_original)
            payee_account_after = "".join(payee_account_after_original.split())     #将输入后的银行卡号空格去掉再对比结果
            print('输入后银行账号：', payee_account_after)

        self.queryTransfer_handle.click_transfer_bank_name_button()
        time.sleep(2)
        payee_bank = self.read_excel.get_cell(4, 10)
        print('payee_bank:',payee_bank)
        self.queryTransfer_handle.click_bank_list_list(payee_bank)
        time.sleep(2)
        self.queryTransfer_handle.click_submit_transfer_button()
        time.sleep(2)

    def query_transferF_select(self):
        '''
        用例编号：111CZSX039,所有功能-查询转账-快速转账
        同行转账-正确输入金额-》步骤：进入快速转账，输入收款人姓名、账号，在银行列表选择同行进行转账，转账金额在（0，余额]之内
        query_transfer_select：从收款人列表中选择账户来转账
        :return:
        '''
        # 选择操作清单
        # print('read_excel方法query_transferF_select:', self.read_excel)
        self.queryTransfer_handle.click_action_list_button('//*[contains(@text,"查询转账")]')
        self.queryTransfer_handle.click_payee_message_button()
        self.queryTransfer_handle.click_transfer_fast_button()
        # 选择账户姓名编辑框右侧的头像按钮
        self.queryTransfer_handle.click_transfer_payee_head_button()
        # 收款人信息页面
        payee_name = self.read_excel.get_cell(5, 8)
        print('payee_name:', payee_name)
        self.queryTransfer_handle.click_bank_list_list(payee_name)
        time.sleep(2)
        self.queryTransfer_handle.click_submit_transfer_button()
        time.sleep(2)

    def query_transfer_page(self, tmRow, tmCol, pwRow, pwCol, rbRow, rbCol):
        '''
        适用于转账，不论快速、普通、次日
        这是在添加完收款人信息后，再进入的转账、验证码、取款密码输入、转账成功的页面
        由于输入银行卡号和选择收款人前面不同流程，但后面的都一致，直接统一维护
        作者：曾志坤，时间：20180411
        :return:
        '''
        # 转账页面
        # transfer_amount = self.read_excel.get_cell(4, 11)
        transfer_amount = self.read_excel.get_cell(tmRow, tmCol)
        print('transfer_amount',transfer_amount)
        self.queryTransfer_handle.send_transfer_amount_code(transfer_amount)
        self.public_method.swipe_on('up', 10000)
        self.queryTransfer_handle.click_transfer_tips_head_button()
        self.queryTransfer_handle.click_submit_transfer_button()
        # 验证码和取款密码输入页面
        self.public_method.swipe_on('up', 10000)
        self.queryTransfer_handle.click_get_code_button()
        self.queryTransfer_handle.send_input_code_code()
        self.queryTransfer_handle.click_draw_password_button()
        # draw_password = self.read_excel.get_cell(4, 7)
        draw_password = self.read_excel.get_cell(pwRow, pwCol)
        print('draw_password',draw_password)
        self.queryTransfer_handle.send_draw_password_code(draw_password)
        self.queryTransfer_handle.click_input_code_code()  # 在输入取款密码后，银行自带键盘会挡住“转账”按钮
        self.queryTransfer_handle.click_transfer_account_submit_button()

        # 在转账时，同一收款人、转账金额有连续两条记录时，则会提示是否需要确认转账
        system_prompts = self.queryTransfer_page.get_system_prompt_element()
        # print('system_prompts:', system_prompts)
        system_prompt = system_prompts[2].get_attribute('text')
        print('获取system_prompt：', system_prompt)
        prompt_tip = '相同的转账交易'
        if prompt_tip in system_prompt:
            self.queryTransfer_handle.click_check_tran_tips_button()
            self.queryTransfer_page.get_error_confirm_element()[0].click()

        # 转账成功页面
        time.sleep(8)
        transfer_submitted_mark = self.queryTransfer_page.get_transfer_submitted_element().get_attribute("text")
        print('转账成功提示：', transfer_submitted_mark)

        transfer_way = self.read_excel.get_cell(tmRow, 4)
        if transfer_way != '次日转账':
            time.sleep(3)
            remaining_balance = self.queryTransfer_page.get_remaining_balance_element().get_attribute("text")
            print('余额：', remaining_balance)
            self.write_excel.write(rbRow, rbCol, remaining_balance)

        self.queryTransfer_handle.click_inform_success_button()  # 点击“好，我知道了”按钮后，跳转到移动银行主页
        time.sleep(5)

        # 如果存在最新公告信息，则判断点击确认
        keyword = '确认'
        confirm = '确认'
        while keyword in confirm:
            confirm_element = self.queryTransfer_page.get_error_confirm_element()
            # print('confirm_element:', confirm_element)
            confirm = confirm_element[0].get_attribute('text')
            # print('弹框信息关键词：', confirm)
            confirm_element[0].click()

        return transfer_submitted_mark

    def query_transferF_payee_space(self):
        '''
        用例编号：111CZSX023,所有功能-查询转账-快速转账
        测试点：同行转账-收款人不填，步骤：收款人信息留空不填，预期结果：温馨提示：请输入收款人信息
        :return:
        '''

        # 选择操作清单
        # print('read_excel方法query_transferF_payee_space:', self.read_excel)
        self.queryTransfer_handle.click_action_list_button('//*[contains(@text,"查询转账")]')
        self.queryTransfer_handle.click_payee_message_button()
        self.queryTransfer_handle.click_transfer_fast_button()
        # 不输入收款人信息，直接点击提交按钮
        time.sleep(2)
        self.queryTransfer_handle.click_submit_transfer_button()
        # 取温馨提示属性，再返回
        # error_prompt = self.driver.find_element_by_id('com.gdnybank.m:id/tv_metion_msg').get_attribute('text')
        error_prompt = self.queryTransfer_page.get_error_prompt_element().get_attribute('text')
        print('温馨提示1：' ,error_prompt)
        self.queryTransfer_handle.click_error_prompt_confirm_button()
        # 返回到转账页面
        self.queryTransfer_handle.click_left_head_button_button()
        # 返回到移动银行主页面
        self.queryTransfer_handle.click_left_head_button_button()
        return error_prompt

    def query_transferF_amount_zero(self):
        '''
        用例编号：111CZSX024,所有功能-查询转账-快速转账
        测试点：同行转账-金额为0，步骤：转账金额为0，预期结果：温馨提示：转账金额输入有误
        :return:
        '''
        # 选择操作清单
        self.query_transferF_select()
        # 转账页面
        self.public_method.swipe_on('up', 10000)
        transfer_amount = self.read_excel.get_cell(7, 11)
        print('transfer_amount:', transfer_amount)
        self.queryTransfer_handle.send_transfer_amount_code(transfer_amount)
        self.queryTransfer_handle.click_transfer_tips_head_button()
        self.queryTransfer_handle.click_submit_transfer_button()
        # 取温馨提示属性，再返回
        error_prompt = self.driver.find_element_by_id('com.gdnybank.m:id/tv_metion_msg').get_attribute('text')
        print('温馨提示2：', error_prompt)
        self.queryTransfer_handle.click_error_prompt_confirm_button()
        # 返回到移动银行主页面
        self.queryTransfer_handle.click_left_head_button_button()
        return error_prompt

    def query_transferF_beyond_balance(self):
        '''
        用例编号：111CZSX025,所有功能-查询转账-快速转账
        测试点：同行转账-超出余额，步骤：转账金额大于可用余额，预期结果：温馨提示：余额不足
        :return:
        '''
        # 选择操作清单
        self.query_transferF_select()
        # 转账页面
        self.public_method.swipe_on('up', 10000)
        transfer_amount = self.read_excel.get_cell(8, 11)
        print('transfer_amount:', transfer_amount)
        self.queryTransfer_handle.send_transfer_amount_code(transfer_amount)
        self.queryTransfer_handle.click_transfer_tips_head_button()
        self.queryTransfer_handle.click_submit_transfer_button()
        # 取温馨提示属性，再返回
        # system_prompt = self.queryTransfer_page.get_system_prompt_element()
        # print('system_prompt:', system_prompt)
        # error_prompt = system_prompt[1].get_attribute('text')
        # print('温馨提示3：', error_prompt)
        #
        # error_prompt = self.driver.find_element_by_id('com.gdnybank.m:id/tv_metion_msg').get_attribute('text')
        # print('温馨提示3：', error_prompt)
        # self.queryTransfer_handle.click_error_prompt_confirm_button()

        # keyword = '确认'
        # confirm = '确认'
        # while keyword in confirm:
        #     confirm_element = self.queryTransfer_page.get_error_confirm_element()
        #     print('confirm_element:', confirm_element)
        #     confirm = confirm_element[0].get_attribute('text')
        #     if confirm == '确认':
        #         print('弹框信息关键词：', confirm)
        #         confirm_element[0].click()

        system_prompt = self.queryTransfer_page.get_system_prompt_element()
        # print('system_prompt:', system_prompt)
        error_prompt = system_prompt[1].get_attribute('text')
        # print('error_prompt:', error_prompt)
        if error_prompt == 'MBS030212':
            confirm_element = self.queryTransfer_page.get_error_confirm_element()
            # print('confirm_element:', confirm_element)
            confirm = confirm_element[0].get_attribute('text')
            if confirm == '确认':
                print('弹框信息关键词：', confirm)
                confirm_element[0].click()
        else:
            # error_prompt = self.driver.find_element_by_id('com.gdnybank.m:id/tv_metion_msg').get_attribute('text')
            error_prompt = self.queryTransfer_page.get_error_prompt_element().get_attribute('text')
            # print('温馨提示3：', error_prompt)
            self.queryTransfer_handle.click_error_prompt_confirm_button()

        # 返回到移动银行主页面
        self.queryTransfer_handle.click_left_head_button_button()
        return error_prompt

    def query_transferF_amount_space(self):
        '''
        用例编号：111CZSX026,所有功能-查询转账-快速转账
        测试点：同行转账-金额不填，步骤：转账金额留空不填，预期结果：温馨提示：请输入转账金额
        :return:
        '''
        # 选择操作清单
        self.query_transferF_select()
        # 转账页面
        self.public_method.swipe_on('up', 10000)
        # self.queryTransfer_handle.send_transfer_amount_code('100000')
        self.queryTransfer_handle.click_transfer_tips_head_button()
        self.queryTransfer_handle.click_submit_transfer_button()
        # 取温馨提示属性，再返回
        error_prompt = self.driver.find_element_by_id('com.gdnybank.m:id/tv_metion_msg').get_attribute('text')
        print('温馨提示4：', error_prompt)
        self.queryTransfer_handle.click_error_prompt_confirm_button()
        # 返回到移动银行主页面
        self.queryTransfer_handle.click_left_head_button_button()
        return error_prompt

    def query_transferF_amount_capital(self):
        '''
        用例编号：111CZSX027,所有功能-查询转账-快速转账
        测试点：同行转账-大写金额，步骤：输入金额后查看大写金额，预期结果：显示正确
        :return:
        '''
        # 选择操作清单
        self.query_transferF_select()
        # 转账页面
        self.public_method.swipe_on('up', 10000)
        transfer_amount = self.read_excel.get_cell(10, 11)
        print('transfer_amount:', transfer_amount)
        self.queryTransfer_handle.send_transfer_amount_code(transfer_amount)
        self.queryTransfer_handle.click_transfer_tips_head_button()
        self.queryTransfer_handle.click_submit_transfer_button()
        # 取温馨提示属性，再返回
        error_prompt = self.driver.find_element_by_id('com.gdnybank.m:id/tv_metion_msg').get_attribute('text')
        print('温馨提示5：', error_prompt)
        self.queryTransfer_handle.click_error_prompt_confirm_button()
        # 返回到移动银行主页面
        self.queryTransfer_handle.click_left_head_button_button()
        return error_prompt

    def query_transferF_payee_wrong(self):
        '''
        用例编号：111CZSX028,所有功能-查询转账-快速转账
        测试点：同行转账-收方信息错误，步骤：进入快速转账，输入收款账号，收款人姓名，开户行三者的任意不匹配，
        预期结果：系统提示：账户和户名不匹配
        :return:error_prompt
        '''
        # 选择操作清单
        self.queryTransfer_handle.click_action_list_button('//*[contains(@text,"查询转账")]')
        self.queryTransfer_handle.click_payee_message_button()
        self.queryTransfer_handle.click_transfer_fast_button()
        # 收款人信息页面,输入错误的收款名
        payee_name = self.read_excel.get_cell(11, 8)
        print('payee_name:', payee_name)
        self.queryTransfer_handle.send_payee_name_code(payee_name)
        # 判断当所输入账号与预期的不一致时，则输入，否则继续下一步选择银行名称
        payee_account = self.read_excel.get_cell(11, 9)
        print('payee_account:', payee_account)
        payee_account_after = 1
        while payee_account != payee_account_after:
            # payee_account = '6235 9574 0000 6141 031'
            # 清除
            self.queryTransfer_handle.clear_payee_account_code()
            time.sleep(5)
            # 输入银行账号
            input_element = self.queryTransfer_page.get_payee_account_element()
            input_element.click()
            self.press_Keycode.press_Keycode(payee_account, input_element)

            # self.queryTransfer_handle.send_payee_account_code(payee_account)
            # 获取输入后的银行账号
            time.sleep(2)
            payee_account_after_original = self.queryTransfer_page.get_payee_input_element()[1].get_attribute("text")
            # print('payee_account_after_original:', payee_account_after_original)
            payee_account_after = "".join(payee_account_after_original.split())  # 将输入后的银行卡号空格去掉再对比结果
            print('输入后银行账号：', payee_account_after)

        self.queryTransfer_handle.click_transfer_bank_name_button()
        time.sleep(2)
        payee_bank = self.read_excel.get_cell(11, 10)
        print('payee_name:', payee_bank)
        self.queryTransfer_handle.click_bank_list_list(payee_bank)
        time.sleep(2)
        self.queryTransfer_handle.click_submit_transfer_button()
        time.sleep(2)
        # 转账页面
        transfer_amount = self.read_excel.get_cell(11, 11)
        print('transfer_amount:',transfer_amount)
        self.queryTransfer_handle.send_transfer_amount_code(transfer_amount)
        self.public_method.swipe_on('up', 10000)
        self.queryTransfer_handle.click_transfer_tips_head_button()
        self.queryTransfer_handle.click_submit_transfer_button()
        # 取温馨提示属性，再返回
        error_prompt = self.driver.find_element_by_id('com.gdnybank.m:id/tv_metion_msg').get_attribute('text')
        print('温馨提示6：', error_prompt)
        self.queryTransfer_handle.click_error_prompt_confirm_button()
        # 返回到移动银行主页面
        self.queryTransfer_handle.click_left_head_button_button()
        return error_prompt

    def query_transferF_same_payer(self):
        '''
        用例编号：111CZSX029,所有功能-查询转账-快速转账
        测试点：同账户转账，步骤：进入快速转账，收款人与付款人为同一人
        预期结果：系统提示：转入转出账户不能相同
        :return:error_prompt
        '''
        # 选择操作清单
        self.queryTransfer_handle.click_action_list_button('//*[contains(@text,"查询转账")]')
        self.queryTransfer_handle.click_payee_message_button()
        self.queryTransfer_handle.click_transfer_fast_button()
        payee_name = self.read_excel.get_cell(12, 8)
        print('payee_name:', payee_name)
        self.queryTransfer_handle.send_payee_name_code(payee_name)
        # 判断当所输入账号与预期的不一致时，则输入，否则继续下一步选择银行名称
        payee_account = self.read_excel.get_cell(12, 9)
        print('payee_account:', payee_account)
        payee_account_after = 1
        while payee_account != payee_account_after:
            # payee_account = '6235 9574 0000 6141 031'
            # 清除
            self.queryTransfer_handle.clear_payee_account_code()
            time.sleep(5)
            # 输入银行账号
            input_element = self.queryTransfer_page.get_payee_account_element()
            input_element.click()
            self.press_Keycode.press_Keycode(payee_account, input_element)

            # self.queryTransfer_handle.send_payee_account_code(payee_account)
            # 获取输入后的银行账号
            time.sleep(2)

            payee_account_after_original = self.queryTransfer_page.get_payee_input_element()[1].get_attribute("text")
            # print('payee_account_after_original:', payee_account_after_original)
            payee_account_after = "".join(payee_account_after_original.split())  # 将输入后的银行卡号空格去掉再对比结果
            print('输入后银行账号：', payee_account_after)

        self.queryTransfer_handle.click_transfer_bank_name_button()
        time.sleep(2)
        payee_bank = self.read_excel.get_cell(12, 10)
        print('payee_name:', payee_bank)
        self.queryTransfer_handle.click_bank_list_list(payee_bank)
        time.sleep(2)
        self.queryTransfer_handle.click_submit_transfer_button()
        time.sleep(2)
        # 转账页面
        transfer_amount = self.read_excel.get_cell(12, 11)
        print('transfer_amount:', transfer_amount)
        self.queryTransfer_handle.send_transfer_amount_code(transfer_amount)
        self.public_method.swipe_on('up', 10000)
        self.queryTransfer_handle.click_transfer_tips_head_button()
        self.queryTransfer_handle.click_submit_transfer_button()
        # 取温馨提示属性，再返回
        # error_prompt = self.driver.find_element_by_id('com.gdnybank.m:id/tv_metion_msg').get_attribute('text')
        error_prompt = self.queryTransfer_page.get_error_prompt_element().get_attribute('text')
        print('温馨提示7：', error_prompt)
        self.queryTransfer_handle.click_error_prompt_confirm_button()
        # 返回到移动银行主页面
        self.queryTransfer_handle.click_left_head_button_button()
        return error_prompt

    def query_transferF_drawpassword_wrong(self):
        '''
        用例编号：111CZSX030，所有功能-查询转账-快速转账
        测试点：密码输入错误，步骤：输入错误密码后提交，预期结果：系统提示：您已输错密码[n]次，再输错[3-n]次，将锁定手机盾
        :return:error_prompt
        '''
        # 选择操作清单
        self.query_transferF_select()
        # 转账页面
        self.public_method.swipe_on('up', 10000)
        transfer_amount = self.read_excel.get_cell(13, 11)
        print('transfer_amount:', transfer_amount)
        self.queryTransfer_handle.send_transfer_amount_code(transfer_amount)
        self.queryTransfer_handle.click_transfer_tips_head_button()
        self.queryTransfer_handle.click_submit_transfer_button()
        # 验证码和取款密码输入页面
        self.public_method.swipe_on('up', 10000)
        self.queryTransfer_handle.click_get_code_button()
        self.queryTransfer_handle.send_input_code_code()
        self.queryTransfer_handle.click_draw_password_button()
        draw_password = self.read_excel.get_cell(13, 7)
        print('draw_password:', draw_password)
        self.queryTransfer_handle.send_draw_password_code(draw_password)
        self.queryTransfer_handle.click_input_code_code()  # 在输入取款密码后，银行自带键盘会挡住“转账”按钮
        self.queryTransfer_handle.click_transfer_account_submit_button()
        # 取温馨提示属性，再返回
        error_prompt = self.driver.find_element_by_id('com.gdnybank.m:id/tv_metion_msg').get_attribute('text')
        print('温馨提示8：', error_prompt)
        self.queryTransfer_handle.click_error_prompt_confirm_button()
        for i in range(2):
            # 返回转账页面
            # 返回到移动银行主页面
            self.queryTransfer_handle.click_left_head_button_button()
        return error_prompt

    def query_transferF_drawpassword_again(self):
        '''
        用例编号：111CZSX031，所有功能-查询转账-快速转账
        测试点：密码输入错误，再输入正确，步骤：输入错误密码次数小于3次，再输入正确密码，点击提交，
        预期结果：成功提交，并且错误次数重置
        :return:transfer_submitted_mark
        '''
        # 取款密码错误
        self.query_transferF_drawpassword_wrong()
        # 取款密码错误后，再次输入正常密码
        self.query_transferF_select()
        # 转账页面
        self.public_method.swipe_on('up', 10000)
        transfer_amount = self.read_excel.get_cell(14, 11)
        print('transfer_amount:', transfer_amount)
        self.queryTransfer_handle.send_transfer_amount_code(transfer_amount)
        self.queryTransfer_handle.click_transfer_tips_head_button()
        self.queryTransfer_handle.click_submit_transfer_button()
        # 转账输入验证码和取款密码页面
        self.public_method.swipe_on('up', 10000)
        self.queryTransfer_handle.click_get_code_button()
        self.queryTransfer_handle.send_input_code_code()
        self.queryTransfer_handle.click_draw_password_button()
        draw_password = self.read_excel.get_cell(14, 7)
        print('draw_password:', draw_password)
        self.queryTransfer_handle.send_draw_password_code(draw_password)
        self.queryTransfer_handle.click_input_code_code()  # 在输入取款密码后，银行自带键盘会挡住“转账”按钮
        self.queryTransfer_handle.click_transfer_account_submit_button()
        # 转账成功页面
        time.sleep(3)
        # transfer_submitted_mark = self.driver.find_element_by_id \
        #     ('com.gdnybank.m:id/tv_repay_already_submit').get_attribute("text")
        transfer_submitted_mark = self.queryTransfer_page.get_transfer_submitted_element().get_attribute("text")
        print('转账成功提示：', transfer_submitted_mark)
        time.sleep(3)
        # remaining_balance = self.driver.find_element_by_id \
        #     ('com.gdnybank.m:id/tv_ava_balance_success').get_attribute("text")
        remaining_balance = self.queryTransfer_page.get_remaining_balance_element().get_attribute("text")
        print('余额：', remaining_balance)
        self.write_excel.write(14,12,remaining_balance)
        self.queryTransfer_handle.click_inform_success_button()  # 点击“好，我知道了”按钮后，跳转到移动银行主页

        keyword = '确认'
        confirm = '确认'
        while keyword in confirm:
            confirm_element = self.queryTransfer_page.get_error_confirm_element()
            # print('confirm_element:', confirm_element)
            confirm = confirm_element[0].get_attribute('text')
            # print('弹框信息关键词：', confirm)
            confirm_element[0].click()
        return transfer_submitted_mark

    def query_transferF_drawpassword_lock(self):
        '''
        用例编号：111CZSX032，所有功能-查询转账-快速转账
        测试点：密码输入错误达到5次锁定，步骤：输入错误密码次数达到3次，点击提交
        预期结果：系统提示：已锁定
        :return:
        '''
        # 选择操作清单
        self.query_transferF_select()
        # 转账页面
        self.public_method.swipe_on('up', 10000)
        transfer_amount = self.read_excel.get_cell(15, 11)
        print('transfer_amount:', transfer_amount)
        self.queryTransfer_handle.send_transfer_amount_code(transfer_amount)
        self.queryTransfer_handle.click_transfer_tips_head_button()
        self.queryTransfer_handle.click_submit_transfer_button()
        # 验证码和取款密码输入页面
        self.public_method.swipe_on('up', 10000)
        self.queryTransfer_handle.click_get_code_button()
        self.queryTransfer_handle.send_input_code_code()
        self.queryTransfer_handle.click_draw_password_button()
        # 输入取款密码错误3次，则锁卡
        for i in range(3):
            draw_password = self.read_excel.get_cell(15, 7)
            print('draw_password:', draw_password)
            self.queryTransfer_handle.send_draw_password_code(draw_password)
            self.queryTransfer_handle.click_input_code_code()  # 在输入取款密码后，银行自带键盘会挡住“转账”按钮
            self.queryTransfer_handle.click_transfer_account_submit_button()
            # 取温馨提示属性，再返回
            error_prompt = self.driver.find_element_by_id('com.gdnybank.m:id/tv_metion_msg').get_attribute('text')
            print('温馨提示9：', error_prompt)
            self.queryTransfer_handle.click_error_prompt_confirm_button()
            return error_prompt
        # 返回转账页面
        self.queryTransfer_handle.click_left_head_button_button()
        # 返回到移动银行主页面
        self.queryTransfer_handle.click_left_head_button_button()
        # return error_prompt


    def query_transferF_drawpassword_lack(self):
        '''
        用例编号：111CZSX033，所有功能-查询转账-快速转账
        测试点：密码输入字数不足，步骤：输入小于6位数的密码，点击提交
        预期结果：取款密码输入不正确，请重新输入
        :return:
        '''
        # 选择操作清单
        self.query_transferF_select()
        # 转账页面
        self.public_method.swipe_on('up', 10000)
        transfer_amount = self.read_excel.get_cell(16, 11)
        print('transfer_amount:', transfer_amount)
        self.queryTransfer_handle.send_transfer_amount_code(transfer_amount)
        self.queryTransfer_handle.click_transfer_tips_head_button()
        self.queryTransfer_handle.click_submit_transfer_button()
        # 验证码和取款密码输入页面
        self.public_method.swipe_on('up', 10000)
        self.queryTransfer_handle.click_get_code_button()
        self.queryTransfer_handle.send_input_code_code()
        self.queryTransfer_handle.click_draw_password_button()
        draw_password = self.read_excel.get_cell(16, 7)
        print('draw_password:', draw_password)
        self.queryTransfer_handle.send_draw_password_code(draw_password)
        self.queryTransfer_handle.click_input_code_code()  # 在输入取款密码后，银行自带键盘会挡住“转账”按钮
        self.queryTransfer_handle.click_transfer_account_submit_button()

        # 取温馨提示属性，再返回
        # error_prompt = self.driver.find_element_by_id('com.gdnybank.m:id/tv_metion_msg').get_attribute('text')
        error_prompt = self.queryTransfer_page.get_error_prompt_element().get_attribute('text')
        print('温馨提示10：', error_prompt)
        self.queryTransfer_handle.click_error_prompt_confirm_button()
        # 返回转账页面
        self.queryTransfer_handle.click_left_head_button_button()
        # 返回到移动银行主页面
        self.queryTransfer_handle.click_left_head_button_button()
        return error_prompt

    def query_transferF_drawpassword_excess(self):
        '''
        用例编号：111CZSX034，所有功能-查询转账-快速转账
        测试点：输入超过6位的密码，步骤：输入超过6位的密码，点击提交
        预期结果：无法输入，最多输入到6位
        :return:
        '''
        # 选择操作清单
        self.query_transferF_select()
        # 转账页面
        self.public_method.swipe_on('up', 10000)
        transfer_amount = self.read_excel.get_cell(17, 11)
        print('transfer_amount:', transfer_amount)
        self.queryTransfer_handle.send_transfer_amount_code(transfer_amount)
        self.queryTransfer_handle.click_transfer_tips_head_button()
        self.queryTransfer_handle.click_submit_transfer_button()
        # 验证码和取款密码输入页面
        self.public_method.swipe_on('up', 10000)
        self.queryTransfer_handle.click_get_code_button()
        self.queryTransfer_handle.send_input_code_code()
        self.queryTransfer_handle.click_draw_password_button()
        draw_password = self.read_excel.get_cell(17, 7)
        print('draw_password:', draw_password)
        self.queryTransfer_handle.send_draw_password_code(draw_password)
        self.queryTransfer_handle.click_input_code_code()  # 在输入取款密码后，银行自带键盘会挡住“转账”按钮
        self.queryTransfer_handle.click_transfer_account_submit_button()

        # 取温馨提示属性，再返回
        # element_exist = self.driver.find_element_by_id('com.gdnybank.m:id/fail_title_tv')
        element_exist = self.queryTransfer_page.get_fail_title_element()
        # print('温馨提示11：', element_exist)
        if element_exist:
            self.queryTransfer_handle.click_error_prompt_confirm_button()
            for i in range(2):
                # 返回转账页面
                # 返回到移动银行主页面
                self.queryTransfer_handle.click_left_head_button_button()
        return element_exist

    def query_transferF_bank_list(self):
        '''
        用例编号：111CZSX035，所有功能-查询转账-快速转账
        测试点：银行列表，步骤：在快速转账里点击“银行名称”
        预期结果：进入银行列表
        :return:
        '''
        # 选择操作清单
        self.queryTransfer_handle.click_action_list_button('//*[contains(@text,"查询转账")]')
        self.queryTransfer_handle.click_payee_message_button()
        self.queryTransfer_handle.click_transfer_fast_button()
        self.queryTransfer_handle.click_transfer_bank_name_button()

        # 取温馨提示属性，再返回
        element_exist = self.queryTransfer_page.get_bank_list_element().is_enabled()
            # self.driver.find_element_by_id('com.gdnybank.m:id/lv_bank_list')
        print('银行列表元素存在：', element_exist)
        if element_exist:
            for i in range(3):
                # 返回收款人信息页面
                # 返回转账页面
                # 返回到移动银行主页面
                self.queryTransfer_handle.click_left_head_button_button()
        return element_exist

    def query_transferF_bank_search(self):
        '''
        用例编号：111CZSX036，所有功能-查询转账-快速转账
        测试点：搜索银行名称，步骤：在银行列表搜索栏里输入银行名称，点击搜索
        预期结果：能搜索出该银行（支持模糊搜索）
        :return:
        '''
        # 选择操作清单
        self.queryTransfer_handle.click_action_list_button('//*[contains(@text,"查询转账")]')
        self.queryTransfer_handle.click_payee_message_button()
        self.queryTransfer_handle.click_transfer_fast_button()
        self.queryTransfer_handle.click_transfer_bank_name_button()
        search_bank = self.read_excel.get_cell(19, 13)
        print('search_bank:',search_bank)
        self.queryTransfer_handle.send_search_bank_code(search_bank)
        self.queryTransfer_handle.click_search_button_button()

        # 取温馨提示属性，再返回
        search_bank_element = self.read_excel.get_cell(19, 14)
        print('search_bank_element:',search_bank_element)
        element_exist = self.queryTransfer_page.get_bank_list_element().find_element_by_xpath(search_bank_element)
        # print('获取银行元素：', element_exist)
        if element_exist:
            for i in range(3):
                # 返回收款人信息页面
                # 返回转账页面
                # 返回到移动银行主页面
                self.queryTransfer_handle.click_left_head_button_button()
        return element_exist

    def query_transferF_payee_list(self):
        '''
        用例编号：111CZSX037，所有功能-查询转账-快速转账
        测试点：收款人名册，步骤：进入快速转账，点击账户姓名右侧的图标
        预期结果：进入收款人列表，列表内显示进行过交易的收款人信息
        :return:
        '''
        # 选择操作清单
        self.queryTransfer_handle.click_action_list_button('//*[contains(@text,"查询转账")]')
        self.queryTransfer_handle.click_payee_message_button()
        self.queryTransfer_handle.click_transfer_fast_button()
        self.queryTransfer_handle.click_transfer_payee_head_button()

        # 取温馨提示属性，再返回
        # 取的是收款人列表的银行卡号元素
        # element_exist = self.driver.find_elements_by_id('com.gdnybank.m:id/tv_card_num')
        element_exist = self.queryTransfer_page.get_bank_list_card_element()
        print('获取收款人列表元素数量：', len(element_exist))
        if element_exist:
            for i in range(3):
                # 返回收款人信息页面
                # 返回转账页面
                # 返回到移动银行主页面
                self.queryTransfer_handle.click_left_head_button_button()
        return element_exist

    def query_transferF_payee_choice(self):
        '''
        用例编号：111CZSX038，所有功能-查询转账-快速转账
        测试点：选择收款人，步骤：在收款人列表，点击其中一个收款人信息
        预期结果：自动返回上一页面，且账户姓名、收款人账号、银行名称已自动填写为选择的收款人信息
        :return:
        '''
        # 选择操作清单
        self.queryTransfer_handle.click_action_list_button('//*[contains(@text,"查询转账")]')
        self.queryTransfer_handle.click_payee_message_button()
        self.queryTransfer_handle.click_transfer_fast_button()
        self.queryTransfer_handle.click_transfer_payee_head_button()

        # 选择收款人页面列表，具体的收款人在excel维护
        payee_name = self.read_excel.get_cell(21, 8)
        print('payee_name:',payee_name)
        self.queryTransfer_handle.click_bank_list_list(payee_name)
        # driver.find_elements_by_class_name("android.wdget.RelativeLayout").__getitem__(1).click()

        # 返回到收款人信息页面，取的是收款人账号元素
        element_code = self.queryTransfer_page.get_payee_account_element().get_attribute("text")
            # self.driver.find_element_by_id('com.gdnybank.m:id/tv_card_num')
        print('获取到的元素：' ,element_code)
        element_length = len(element_code)
        print('元素长度：', element_length)
        element_compare = (element_length > 8)  # 考虑到还没输入账号时，是5位字符，账号可能至少有8位
        if element_compare:
            for i in range(2):
                # 返回转账页面
                # 返回到移动银行主页面
                self.queryTransfer_handle.click_left_head_button_button()
        return element_compare

    def query_transferF_payee_add(self):
        '''
        用例编号：111CZSX039，所有功能-查询转账-快速转账
        测试点：添加收款人，步骤：进行一笔快速转账交易
        预期结果：交易成功后自动将该收款人添加进收款人名册
        :return: payeelist_compare
        '''

        # 选择操作清单
        self.queryTransfer_handle.click_action_list_button('//*[contains(@text,"查询转账")]')
        self.queryTransfer_handle.click_payee_message_button()
        self.queryTransfer_handle.click_transfer_fast_button()
        self.queryTransfer_handle.click_transfer_payee_head_button()

        # 添加收款人前的收款人清单数量
        # payeelist_before = self.queryTransfer_page.get_bank_list_card_element()
        # print('添加前元素：' ,payeelist_before)
        payeelist_length_before = len(self.queryTransfer_page.get_bank_list_card_element())
        print('添加前：' ,payeelist_length_before)

        # 返回转账页面
        self.queryTransfer_handle.click_left_head_button_button()
        payee_name = self.read_excel.get_cell(22, 8)
        print('payee_name:',payee_name)
        self.queryTransfer_handle.send_payee_name_code(payee_name)

        # 判断当所输入账号与预期的不一致时，则输入，否则继续下一步选择银行名称
        payee_account = self.read_excel.get_cell(22, 9)
        print('payee_account:',payee_account)
        payee_account_after = 1
        while payee_account != payee_account_after:
            # payee_account = '6235 9574 0000 6141 031'
            # 清除
            self.queryTransfer_handle.clear_payee_account_code()
            time.sleep(5)
            # 输入银行账号
            input_element = self.queryTransfer_page.get_payee_account_element()
            input_element.click()
            self.press_Keycode.press_Keycode(payee_account, input_element)

            # self.queryTransfer_handle.send_payee_account_code(payee_account)
            # 获取输入后的银行账号
            time.sleep(2)

            payee_account_after_original = self.queryTransfer_page.get_payee_input_element()[1].get_attribute("text")
            # print('payee_account_after_original:', payee_account_after_original)
            payee_account_after = "".join(payee_account_after_original.split())  # 将输入后的银行卡号空格去掉再对比结果
            print('输入后银行账号：', payee_account_after)

        self.queryTransfer_handle.click_transfer_bank_name_button()
        time.sleep(2)
        payee_bank = self.read_excel.get_cell(22, 10)
        print('payee_bank:', payee_bank)
        self.queryTransfer_handle.click_bank_list_list(payee_bank)
        time.sleep(2)
        self.queryTransfer_handle.click_submit_transfer_button()
        time.sleep(2)
        # 调用转账页面方法
        self.query_transfer_page(22, 11, 22, 7, 22, 12)

        # 选择操作清单
        self.queryTransfer_handle.click_action_list_button('//*[contains(@text,"查询转账")]')
        self.queryTransfer_handle.click_payee_message_button()
        self.queryTransfer_handle.click_transfer_fast_button()
        self.queryTransfer_handle.click_transfer_payee_head_button()

        # 添加新的收款人后的收款人清单数量
        # payeelist_after = self.queryTransfer_page.get_bank_list_card_element()
        payeelist_length_after = len(self.queryTransfer_page.get_bank_list_card_element())
        print('添加后：' , payeelist_length_after)
        payeelist_compare = (payeelist_length_before < payeelist_length_after)
        print('对比结果：', payeelist_compare)
        if payeelist_compare:
            for i in range(3):
                # 返回收款人信息页面
                # 返回转账页面
                # 返回到移动银行主页面
                self.queryTransfer_handle.click_left_head_button_button()

        keyword = '确认'
        confirm = '确认'
        while keyword in confirm:
            confirm_element = self.queryTransfer_page.get_error_confirm_element()
            # print('confirm_element:', confirm_element)
            confirm = confirm_element[0].get_attribute('text')
            # print('弹框信息关键词：', confirm)
            confirm_element[0].click()
        return payeelist_compare

    def query_transferF_payee_delete_before(self):
        '''
        用例编号：111CZSX040，所有功能-查询转账-快速转账
        测试点：删除收款人，步骤：在收款人列表，点击右上角编辑，然后点击某收款人左侧删除按钮
        预期结果：成功删除该收款人信息
        本方法是记录删除前得到需要删除的选项，返回i
        :return: i
        '''
        # 选择操作清单
        self.queryTransfer_handle.click_action_list_button('//*[contains(@text,"查询转账")]')
        self.queryTransfer_handle.click_payee_message_button()
        self.queryTransfer_handle.click_transfer_fast_button()
        self.queryTransfer_handle.click_transfer_payee_head_button()

        self.queryTransfer_handle.click_payee_list_edit_button()
        # 获取要删除的收款人元素-》再获取按照银行名称查询的id定位元素-》for再while语句判断删除收款人元素排在第几位，得到i+1
        # 最后使用删除按钮find_elements_by_id('删除id')[i+1].click()
        # target_element = self.queryTransfer_page.get_bank_list_element() \
        #     .find_element_by_xpath('//*[contains(@text,"A3338")]')
        payee_name_target = self.read_excel.get_cell(23, 15)
        print('payee_name_target:',payee_name_target)

        # targets_element = self.driver.find_elements_by_id('com.gdnybank.m:id/tv_name_payee_contant_item')
        targets_element = self.queryTransfer_page.get_payee_list_name_element()
        # print('收款人列表元素：' ,targets_element)
        targets_element_length = len(targets_element)
        print('收款人列表元素长度：' ,targets_element_length)
        for i in range(targets_element_length):
            payee_name = targets_element[i].get_attribute('text')
            print('第'+str(i)+'收款人名字：',payee_name)
            if payee_name_target == payee_name:
                print('收款人元素数组：', i)
                return i

    def query_transferF_payee_delete(self):
        '''
        用例编号：111CZSX040，所有功能-查询转账-快速转账
        测试点：删除收款人，步骤：在收款人列表，点击右上角编辑，然后点击某收款人左侧删除按钮
        预期结果：成功删除该收款人信息
        :return: payeelist_compare_length
        '''
        # 调用删除前需要删除的元素第几位元素
        j = self.query_transferF_payee_delete_before()
        print('取到值：',j)
        # 删除收款人前的收款人清单数量
        payeelist_length_before = len(self.queryTransfer_page.get_bank_list_card_element())
        print('删除前长度：' ,payeelist_length_before)
        # delete_element= self.driver.find_elements_by_id('com.gdnybank.m:id/btn_del_payee_contact_item')[j]
        delete_element = self.queryTransfer_page.get_payee_delete_element()[j]
        delete_element.click()
        # self.queryTransfer_handle.click_payee_delete_button()
        payeelist_length_after = len(self.queryTransfer_page.get_bank_list_card_element())
        print('删除后长度：',payeelist_length_after)
        payeelist_compare = (payeelist_length_before > payeelist_length_after)
        print('对比结果：', payeelist_compare)
        if payeelist_compare:
            self.queryTransfer_handle.click_payee_list_complete_button()
            for i in range(3):
                # 返回收款人信息页面
                # 返回转账页面
                # 返回到移动银行主页面
                self.queryTransfer_handle.click_left_head_button_button()
        return payeelist_compare


    def query_transferF_payee_cityChoice(self):
        '''
        用例编号：111CZSX041，所有功能-查询转账-快速转账
        测试点：收款支行选择，步骤：点击银行名称进入银行列表，点击某其他银行
        预期结果：进入支行选择页面
        :return:
        '''
        # 选择操作清单
        self.queryTransfer_handle.click_action_list_button('//*[contains(@text,"查询转账")]')
        self.queryTransfer_handle.click_payee_message_button()
        self.queryTransfer_handle.click_transfer_fast_button()
        # self.queryTransfer_handle.click_transfer_payee_head_button()

        self.queryTransfer_handle.click_transfer_bank_name_button()
        payee_bank = self.read_excel.get_cell(24, 13)
        print('payee_bank:', payee_bank)
        self.queryTransfer_handle.click_bank_list_list(payee_bank)
        # 进入南粤银行以外的银行，显示支行信息
        # 获取支行页面的关键字来验证
        self.queryTransfer_handle.click_search_city_button()
        # 如果选择非广州的城市，则需要先查询，但如果是热门城市，搜索再选择，会有两个搜索结果
        # self.queryTransfer_handle.send_search_city_code('广州')
        # self.queryTransfer_handle.click_city_branch_search_button()
        # 可能是find_elements
        city = self.read_excel.get_cell(24, 16)
        print('city:', city)
        # citys_element = self.driver.find_elements_by_id('com.gdnybank.m:id/city')
        citys_element = self.queryTransfer_page.get_city_list_element()
        # print('城市列表元素：' ,citys_element)
        citys_element_length = len(citys_element)
        print('城市列表元素长度：', citys_element_length)
        for i in range(citys_element_length):
            city_name = citys_element[i].get_attribute('text')
            print('第' + str(i) + '城市：', city_name)
            if city == city_name:
                # print('城市元素数组：', i)
                return i

    def query_transferF_payee_branch(self):
        '''
        用例编号：111CZSX041，所有功能-查询转账-快速转账
        测试点：收款支行选择，步骤：点击银行名称进入银行列表，点击某其他银行
        预期结果：进入支行选择页面
        :return:
        '''
        # 调用查看前需要搜索城市在第几位元素
        j = self.query_transferF_payee_cityChoice()
        # print('城市元素取到值：',j)
        city_elements= self.queryTransfer_page.get_city_list_element()[j]
        city_elements.click()
        self.queryTransfer_handle.click_branch_search_button()
        branch_amount = self.queryTransfer_page.get_branch_bank_amount_element().get_attribute('text')
        print('获取的属性：', branch_amount)
        branch_amountRe = re.sub("\D", "", branch_amount)
        print('抽取出来的数字有：', branch_amountRe)
        compare_branch_amount = branch_amountRe > '0'
        if compare_branch_amount:
            for i in range(4):
                self.queryTransfer_handle.click_left_head_button_button()
        return compare_branch_amount

    def query_transferF_payee_city(self):
        '''
        用例编号：111CZSX042，所有功能-查询转账-快速转账
        测试点：选择转入账号城市，步骤：点击城市名称搜索栏
        预期结果：弹出城市列表
        :return:
        '''
        # 选择操作清单
        self.queryTransfer_handle.click_action_list_button('//*[contains(@text,"查询转账")]')
        self.queryTransfer_handle.click_payee_message_button()
        self.queryTransfer_handle.click_transfer_fast_button()
        # self.queryTransfer_handle.click_transfer_payee_head_button()

        self.queryTransfer_handle.click_transfer_bank_name_button()
        payee_bank = self.read_excel.get_cell(25, 13)
        print('payee_bank:',payee_bank)
        self.queryTransfer_handle.click_bank_list_list(payee_bank)
        # 进入南粤银行以外的银行，显示支行信息
        # 获取支行页面的关键字来验证

        self.queryTransfer_handle.click_search_city_button()
        verify_title = '城市列表'
        city_list = self.queryTransfer_page.get_title_head_element().get_attribute('text')
        print('获取到的头条标题：',city_list)
        city_compare = (city_list == verify_title)
        print('城市列表对比结果：', city_compare)
        if city_list == verify_title:
            for i in range(5):
                self.queryTransfer_handle.click_left_head_button_button()
        return city_list

    def query_transferF_branch_keyword(self):
        '''
        用例编号：111CZSX043，所有功能-查询转账-快速转账
        测试点：支行关键字搜索，步骤：选择城市后，输入关键字进行搜索
        预期结果：成功搜索出该城市下有该关键字的支行
        :return:
        '''
        # 调用查看前需要搜索城市在第几位元素
        j = self.query_transferF_payee_cityChoice()
        print('城市元素取到值：',j)
        city_elements= self.queryTransfer_page.get_city_list_element()[j]
        city_elements.click()
        self.queryTransfer_handle.click_branch_search_button()
        time.sleep(5)
        branch_amount = self.queryTransfer_page.get_branch_bank_amount_element().get_attribute('text')
        print('获取的属性：', branch_amount)
        branch_amountRe = re.sub("\D", "", branch_amount)
        print('抽取出来的数字有：', branch_amountRe)
        compare_branch_amount = branch_amountRe > '0'
        if compare_branch_amount:
            print('查询分行信息正常')
        branchKeyword = self.read_excel.get_cell(26 ,17)
        self.queryTransfer_handle.send_branch_keyword_code(branchKeyword)
        self.queryTransfer_handle.click_branch_search_button()
        branch_bank = self.queryTransfer_page.get_branch_bank_keyword_element()
        # print('分行查询结果元素：',branch_bank)
        if branch_bank != None:
            for i in range(4):
                self.queryTransfer_handle.click_left_head_button_button()
        return branch_bank


    def query_transferF_account_detail(self):
        '''
        用例编号：111CZSX044，所有功能-查询转账-快速转账
        测试点：查看账户详情，步骤：点击卡片右下角的感叹号
        预期结果：进入对应账户的详情页面
        :return:
        '''
        # 选择操作清单
        self.queryTransfer_handle.click_action_list_button('//*[contains(@text,"查询转账")]')
        time.sleep(2)
        self.queryTransfer_handle.click_account_plaint_button()
        # 获取账户详情的元素
        # 再打印账户详情的信息点到excel
        account_amount = len(self.queryTransfer_page.get_account_types_element())
        print('账户种类：', account_amount)
        account_message = []
        if account_amount > 0 :
            for i in range(account_amount):
                account_types = self.queryTransfer_page.get_account_types_element()
                account_balances = self.queryTransfer_page.get_account_balance_element()
                regist_dates = self.queryTransfer_page.get_regist_date_element()
                acc_type = "acc_type" + str(i)
                account_balance = "account_balance" + str(i)
                regist_date = "regist_date" + str(i)
                print('赋值：',acc_type,",",account_balance,",",regist_date)
                acc_type = account_types[i].get_attribute('text')
                account_balance = account_balances[i].get_attribute('text')
                regist_date = regist_dates[i].get_attribute('text')
                account_message.append(acc_type)
                account_message.append(account_balance)
                account_message.append(regist_date)
                print('第' + str(i) + '账户种类：',acc_type)
                print('第' + str(i) + '账户余额：',account_balance)
                print('第' + str(i) + '开户日期：', regist_date)
                print('列表：',account_message)
                # self.write_excel.write(27, 18, account_message)
            print('列表account_message：', account_message)
            account_message_str =  ",".join(account_message)
            print('列表转换为字符串：', account_message_str)
            self.write_excel.write(27, 18, account_message_str)

            for j in range(2):
                self.queryTransfer_handle.click_left_head_button_button()
        else:
            return None
        return account_amount
    #--------------------------------------------查询转账->普通转账------------------------------------------------------
    '''
    查询转账->普通转账
    '''
    def query_transferG_select(self):
        '''
        用例编号：111CZSX039,所有功能-查询转账-快速转账
        同行转账-正确输入金额-》步骤：进入快速转账，输入收款人姓名、账号，在银行列表选择同行进行转账，转账金额在（0，余额]之内
        query_transfer_select：从收款人列表中选择账户来转账
        :return:
        '''
        # 选择操作清单
        self.queryTransfer_handle.click_action_list_button('//*[contains(@text,"查询转账")]')
        self.queryTransfer_handle.click_payee_message_button()
        self.queryTransfer_handle.click_transfer_other_button()
        # 选择账户姓名编辑框右侧的头像按钮
        self.queryTransfer_handle.click_transfer_payee_head_button()
        # 收款人信息页面
        payee_name = self.read_excel.get_cell(28, 8)
        print('payee_name:', payee_name)
        self.queryTransfer_handle.click_bank_list_list(payee_name)
        time.sleep(2)
        self.queryTransfer_handle.click_submit_transfer_button()
        time.sleep(2)

    def query_transferG_amount_zero(self):
        '''
        用例编号：111CZSX024,所有功能-查询转账-快速转账
        测试点：同行转账-金额为0，步骤：转账金额为0，预期结果：温馨提示：转账金额输入有误
        :return:
        '''
        # 选择操作清单
        self.query_transferG_select()
        # 转账页面
        self.public_method.swipe_on('up', 10000)
        transfer_amount = self.read_excel.get_cell(29, 11)
        print('transfer_amount:', transfer_amount)
        self.queryTransfer_handle.send_transfer_amount_code(transfer_amount)
        self.queryTransfer_handle.click_transfer_tips_head_button()
        self.queryTransfer_handle.click_submit_transfer_button()
        # 取温馨提示属性，再返回
        error_prompt = self.driver.find_element_by_id('com.gdnybank.m:id/tv_metion_msg').get_attribute('text')
        print('温馨提示2：', error_prompt)
        self.queryTransfer_handle.click_error_prompt_confirm_button()
        # 返回到移动银行主页面
        self.queryTransfer_handle.click_left_head_button_button()
        return error_prompt

    def query_transferG_beyond_balance(self):
        '''
        用例编号：111CZSX025,所有功能-查询转账-快速转账
        测试点：同行转账-超出余额，步骤：转账金额大于可用余额，预期结果：温馨提示：余额不足
        :return:
        '''
        # 选择操作清单
        self.query_transferG_select()
        # 转账页面
        self.public_method.swipe_on('up', 10000)
        transfer_amount = self.read_excel.get_cell(30, 11)
        print('transfer_amount:', transfer_amount)
        self.queryTransfer_handle.send_transfer_amount_code(transfer_amount)
        self.queryTransfer_handle.click_transfer_tips_head_button()
        self.queryTransfer_handle.click_submit_transfer_button()
        # 取温馨提示属性，再返回
        error_prompt = self.driver.find_element_by_id('com.gdnybank.m:id/tv_metion_msg').get_attribute('text')
        print('温馨提示3：', error_prompt)
        self.queryTransfer_handle.click_error_prompt_confirm_button()
        # 返回到移动银行主页面
        self.queryTransfer_handle.click_left_head_button_button()
        return error_prompt

    def query_transferG_amount_space(self):
        '''
        用例编号：111CZSX026,所有功能-查询转账-快速转账
        测试点：同行转账-金额不填，步骤：转账金额留空不填，预期结果：温馨提示：请输入转账金额
        :return:
        '''
        # 选择操作清单
        self.query_transferG_select()
        # 转账页面
        self.public_method.swipe_on('up', 10000)
        # self.queryTransfer_handle.send_transfer_amount_code('100000')
        self.queryTransfer_handle.click_transfer_tips_head_button()
        self.queryTransfer_handle.click_submit_transfer_button()
        # 取温馨提示属性，再返回
        error_prompt = self.driver.find_element_by_id('com.gdnybank.m:id/tv_metion_msg').get_attribute('text')
        print('温馨提示4：', error_prompt)
        self.queryTransfer_handle.click_error_prompt_confirm_button()
        # 返回到移动银行主页面
        self.queryTransfer_handle.click_left_head_button_button()
        return error_prompt

    def query_transferG_amount_capital(self):
        '''
        用例编号：111CZSX027,所有功能-查询转账-快速转账
        测试点：同行转账-大写金额，步骤：输入金额后查看大写金额，预期结果：显示正确
        :return:
        '''
        # 选择操作清单
        self.query_transferG_select()
        # 转账页面
        self.public_method.swipe_on('up', 10000)
        transfer_amount = self.read_excel.get_cell(32, 11)
        print('transfer_amount:', transfer_amount)
        self.queryTransfer_handle.send_transfer_amount_code(transfer_amount)
        self.queryTransfer_handle.click_transfer_tips_head_button()
        self.queryTransfer_handle.click_submit_transfer_button()
        # 取温馨提示属性，再返回
        error_prompt = self.driver.find_element_by_id('com.gdnybank.m:id/tv_metion_msg').get_attribute('text')
        print('温馨提示5：', error_prompt)
        self.queryTransfer_handle.click_error_prompt_confirm_button()
        # 返回到移动银行主页面
        self.queryTransfer_handle.click_left_head_button_button()
        return error_prompt

    def query_transferG_payee_wrong(self):
        '''
        用例编号：111CZSX028,所有功能-查询转账-快速转账
        测试点：同行转账-收方信息错误，步骤：进入快速转账，输入收款账号，收款人姓名，开户行三者的任意不匹配，
        预期结果：系统提示：账户和户名不匹配
        :return:error_prompt
        '''
        # 选择操作清单
        self.queryTransfer_handle.click_action_list_button('//*[contains(@text,"查询转账")]')
        self.queryTransfer_handle.click_payee_message_button()
        self.queryTransfer_handle.click_transfer_other_button()
        # 收款人信息页面,输入错误的收款名
        payee_name = self.read_excel.get_cell(33, 8)
        print('payee_name:', payee_name)
        self.queryTransfer_handle.send_payee_name_code(payee_name)
        # 判断当所输入账号与预期的不一致时，则输入，否则继续下一步选择银行名称
        payee_account = self.read_excel.get_cell(33, 9)
        print('payee_account:', payee_account)
        payee_account_after = 1
        while payee_account != payee_account_after:
            # payee_account = '6235 9574 0000 6141 031'
            # 清除
            self.queryTransfer_handle.clear_payee_account_code()
            time.sleep(5)
            # 输入银行账号
            input_element = self.queryTransfer_page.get_payee_account_element()
            input_element.click()
            self.press_Keycode.press_Keycode(payee_account, input_element)

            # self.queryTransfer_handle.send_payee_account_code(payee_account)
            # 获取输入后的银行账号
            time.sleep(2)

            payee_account_after_original = self.queryTransfer_page.get_payee_input_element()[1].get_attribute("text")
            payee_account_after = "".join(payee_account_after_original.split())  # 将输入后的银行卡号空格去掉再对比结果
            print('输入后银行账号：', payee_account_after)

        self.queryTransfer_handle.click_transfer_bank_name_button()
        time.sleep(2)
        payee_bank = self.read_excel.get_cell(33, 10)
        print('payee_name:', payee_bank)
        self.queryTransfer_handle.click_bank_list_list(payee_bank)
        time.sleep(2)
        self.queryTransfer_handle.click_submit_transfer_button()
        time.sleep(2)
        # 转账页面
        transfer_amount = self.read_excel.get_cell(33, 11)
        print('transfer_amount:', transfer_amount)
        self.queryTransfer_handle.send_transfer_amount_code(transfer_amount)
        self.public_method.swipe_on('up', 10000)
        self.queryTransfer_handle.click_transfer_tips_head_button()
        self.queryTransfer_handle.click_submit_transfer_button()
        # 取温馨提示属性，再返回
        error_prompt = self.driver.find_element_by_id('com.gdnybank.m:id/tv_metion_msg').get_attribute('text')
        print('温馨提示6：', error_prompt)
        self.queryTransfer_handle.click_error_prompt_confirm_button()
        # 返回到移动银行主页面
        self.queryTransfer_handle.click_left_head_button_button()
        return error_prompt

    def query_transferG_payee_space(self):
        '''
        用例编号：111CZSX023,所有功能-查询转账-快速转账
        测试点：同行转账-收款人不填，步骤：收款人信息留空不填，预期结果：温馨提示：请输入收款人信息
        :return:
        '''

        # 选择操作清单
        # print('read_excel方法query_transferF_payee_space:', self.read_excel)
        self.queryTransfer_handle.click_action_list_button('//*[contains(@text,"查询转账")]')
        self.queryTransfer_handle.click_payee_message_button()
        self.queryTransfer_handle.click_transfer_other_button()
        # 不输入收款人信息，直接点击提交按钮
        time.sleep(2)
        self.queryTransfer_handle.click_submit_transfer_button()
        # 取温馨提示属性，再返回
        error_prompt = self.queryTransfer_page.get_error_prompt_element().get_attribute('text')
        print('温馨提示1：' ,error_prompt)
        self.queryTransfer_handle.click_error_prompt_confirm_button()
        # 返回到转账页面
        self.queryTransfer_handle.click_left_head_button_button()
        # 返回到移动银行主页面
        self.queryTransfer_handle.click_left_head_button_button()
        return error_prompt

    def query_transferG_same_payer(self):
        '''
        用例编号：111CZSX029,所有功能-查询转账-快速转账
        测试点：同账户转账，步骤：进入快速转账，收款人与付款人为同一人
        预期结果：系统提示：转入转出账户不能相同
        :return:error_prompt
        '''
        # 选择操作清单
        self.queryTransfer_handle.click_action_list_button('//*[contains(@text,"查询转账")]')
        self.queryTransfer_handle.click_payee_message_button()
        self.queryTransfer_handle.click_transfer_other_button()
        payee_name = self.read_excel.get_cell(35, 8)
        print('payee_name:', payee_name)
        self.queryTransfer_handle.send_payee_name_code(payee_name)
        # 判断当所输入账号与预期的不一致时，则输入，否则继续下一步选择银行名称
        payee_account = self.read_excel.get_cell(35, 9)
        print('payee_account:', payee_account)
        payee_account_after = 1
        while payee_account != payee_account_after:
            # payee_account = '6235 9574 0000 6141 031'
            # 清除
            self.queryTransfer_handle.clear_payee_account_code()
            time.sleep(5)
            # 输入银行账号
            input_element = self.queryTransfer_page.get_payee_account_element()
            input_element.click()
            self.press_Keycode.press_Keycode(payee_account, input_element)

            # self.queryTransfer_handle.send_payee_account_code(payee_account)
            # 获取输入后的银行账号
            time.sleep(2)

            payee_account_after_original = self.queryTransfer_page.get_payee_input_element()[1].get_attribute("text")
            # print('payee_account_after_original:', payee_account_after_original)
            payee_account_after = "".join(payee_account_after_original.split())  # 将输入后的银行卡号空格去掉再对比结果
            print('输入后银行账号：', payee_account_after)

        self.queryTransfer_handle.click_transfer_bank_name_button()
        time.sleep(2)
        payee_bank = self.read_excel.get_cell(35,10)
        print('payee_bank:', payee_bank)
        self.queryTransfer_handle.click_bank_list_list(payee_bank)
        time.sleep(2)
        self.queryTransfer_handle.click_submit_transfer_button()
        time.sleep(2)
        # 转账页面
        transfer_amount = self.read_excel.get_cell(35, 11)
        print('transfer_amount:', transfer_amount)
        self.queryTransfer_handle.send_transfer_amount_code(transfer_amount)
        self.public_method.swipe_on('up', 10000)
        self.queryTransfer_handle.click_transfer_tips_head_button()
        self.queryTransfer_handle.click_submit_transfer_button()
        # 取温馨提示属性，再返回
        error_prompt = self.queryTransfer_page.get_error_prompt_element().get_attribute('text')
        print('温馨提示7：', error_prompt)
        self.queryTransfer_handle.click_error_prompt_confirm_button()
        # 返回到移动银行主页面
        self.queryTransfer_handle.click_left_head_button_button()
        return error_prompt

    def query_transferG_drawpassword_wrong(self):
        '''
        用例编号：111CZSX030，所有功能-查询转账-快速转账
        测试点：密码输入错误，步骤：输入错误密码后提交，预期结果：系统提示：您已输错密码[n]次，再输错[3-n]次，将锁定手机盾
        :return:error_prompt
        '''
        # 选择操作清单
        self.query_transferG_select()
        # 转账页面
        self.public_method.swipe_on('up', 10000)
        transfer_amount = self.read_excel.get_cell(36, 11)
        print('transfer_amount:', transfer_amount)
        self.queryTransfer_handle.send_transfer_amount_code(transfer_amount)
        self.queryTransfer_handle.click_transfer_tips_head_button()
        self.queryTransfer_handle.click_submit_transfer_button()
        # 验证码和取款密码输入页面
        self.public_method.swipe_on('up', 10000)
        self.queryTransfer_handle.click_get_code_button()
        self.queryTransfer_handle.send_input_code_code()
        self.queryTransfer_handle.click_draw_password_button()
        draw_password = self.read_excel.get_cell(36, 7)
        print('draw_password:', draw_password)
        self.queryTransfer_handle.send_draw_password_code(draw_password)
        self.queryTransfer_handle.click_input_code_code()  # 在输入取款密码后，银行自带键盘会挡住“转账”按钮
        self.queryTransfer_handle.click_transfer_account_submit_button()
        # 取温馨提示属性，再返回
        error_prompt = self.driver.find_element_by_id('com.gdnybank.m:id/tv_metion_msg').get_attribute('text')
        print('温馨提示8：', error_prompt)
        self.queryTransfer_handle.click_error_prompt_confirm_button()
        for i in range(2):
            # 返回转账页面
            # 返回到移动银行主页面
            self.queryTransfer_handle.click_left_head_button_button()
        return error_prompt

    def query_transferG_drawpassword_again(self):
        '''
        用例编号：111CZSX031，所有功能-查询转账-快速转账
        测试点：密码输入错误，再输入正确，步骤：输入错误密码次数小于3次，再输入正确密码，点击提交，
        预期结果：成功提交，并且错误次数重置
        :return:transfer_submitted_mark
        '''
        # 取款密码错误
        self.query_transferG_drawpassword_wrong()
        # 取款密码错误后，再次输入正常密码
        self.query_transferG_select()

        # 转账页面
        self.public_method.swipe_on('up', 10000)
        transfer_amount = self.read_excel.get_cell(37, 11)
        print('transfer_amount:', transfer_amount)
        self.queryTransfer_handle.send_transfer_amount_code(transfer_amount)
        self.queryTransfer_handle.click_transfer_tips_head_button()
        self.queryTransfer_handle.click_submit_transfer_button()

        # 转账输入验证码和取款密码页面
        self.public_method.swipe_on('up', 10000)
        self.queryTransfer_handle.click_get_code_button()
        self.queryTransfer_handle.send_input_code_code()
        self.queryTransfer_handle.click_draw_password_button()
        draw_password = self.read_excel.get_cell(37, 7)
        print('draw_password:', draw_password)
        self.queryTransfer_handle.send_draw_password_code(draw_password)
        self.queryTransfer_handle.click_input_code_code()  # 在输入取款密码后，银行自带键盘会挡住“转账”按钮
        self.queryTransfer_handle.click_transfer_account_submit_button()

        # 转账成功页面
        time.sleep(3)
        transfer_submitted_mark = self.queryTransfer_page.get_transfer_submitted_element().get_attribute("text")
        print('转账成功提示：', transfer_submitted_mark)
        time.sleep(3)
        remaining_balance = self.queryTransfer_page.get_remaining_balance_element().get_attribute("text")
        print('余额：', remaining_balance)
        self.write_excel.write(37,12,remaining_balance)
        self.queryTransfer_handle.click_inform_success_button()  # 点击“好，我知道了”按钮后，跳转到移动银行主页

        keyword = '确认'
        confirm = '确认'
        while keyword in confirm:
            confirm_element = self.queryTransfer_page.get_error_confirm_element()
            # print('confirm_element:', confirm_element)
            confirm = confirm_element[0].get_attribute('text')
            # print('弹框信息关键词：', confirm)
            confirm_element[0].click()
        return transfer_submitted_mark

    def query_transferG_drawpassword_lock(self):
        '''
        用例编号：111CZSX032，所有功能-查询转账-快速转账
        测试点：密码输入错误达到5次锁定，步骤：输入错误密码次数达到3次，点击提交
        预期结果：系统提示：已锁定
        :return:
        '''
        # 选择操作清单
        self.query_transferG_select()
        # 转账页面
        self.public_method.swipe_on('up', 10000)
        transfer_amount = self.read_excel.get_cell(14, 10)
        print('transfer_amount:', transfer_amount)
        self.queryTransfer_handle.send_transfer_amount_code(transfer_amount)
        self.queryTransfer_handle.click_transfer_tips_head_button()
        self.queryTransfer_handle.click_submit_transfer_button()
        # 验证码和取款密码输入页面
        self.public_method.swipe_on('up', 10000)
        self.queryTransfer_handle.click_get_code_button()
        self.queryTransfer_handle.send_input_code_code()
        self.queryTransfer_handle.click_draw_password_button()
        # 输入取款密码错误3次，则锁卡
        for i in range(3):
            draw_password = self.read_excel.get_cell(14, 6)
            print('draw_password:', draw_password)
            self.queryTransfer_handle.send_draw_password_code(draw_password)
            self.queryTransfer_handle.click_input_code_code()  # 在输入取款密码后，银行自带键盘会挡住“转账”按钮
            self.queryTransfer_handle.click_transfer_account_submit_button()
            # 取温馨提示属性，再返回
            error_prompt = self.driver.find_element_by_id('com.gdnybank.m:id/tv_metion_msg').get_attribute('text')
            print('温馨提示9：', error_prompt)
            self.queryTransfer_handle.click_error_prompt_confirm_button()
            return error_prompt
        # 返回转账页面
        self.queryTransfer_handle.click_left_head_button_button()
        # 返回到移动银行主页面
        self.queryTransfer_handle.click_left_head_button_button()
        # return error_prompt

    def query_transferG_drawpassword_lack(self):
        '''
        用例编号：111CZSX033，所有功能-查询转账-快速转账
        测试点：密码输入字数不足，步骤：输入小于6位数的密码，点击提交
        预期结果：取款密码输入不正确，请重新输入
        :return:
        '''
        # 选择操作清单
        self.query_transferG_select()
        # 转账页面
        self.public_method.swipe_on('up', 10000)
        transfer_amount = self.read_excel.get_cell(38, 11)
        print('transfer_amount:', transfer_amount)
        self.queryTransfer_handle.send_transfer_amount_code(transfer_amount)
        self.queryTransfer_handle.click_transfer_tips_head_button()
        self.queryTransfer_handle.click_submit_transfer_button()
        # 验证码和取款密码输入页面
        self.public_method.swipe_on('up', 10000)
        self.queryTransfer_handle.click_get_code_button()
        self.queryTransfer_handle.send_input_code_code()
        self.queryTransfer_handle.click_draw_password_button()
        draw_password = self.read_excel.get_cell(38, 7)
        print('draw_password:', draw_password)
        self.queryTransfer_handle.send_draw_password_code(draw_password)
        self.queryTransfer_handle.click_input_code_code()  # 在输入取款密码后，银行自带键盘会挡住“转账”按钮
        self.queryTransfer_handle.click_transfer_account_submit_button()

        # 取温馨提示属性，再返回
        error_prompt = self.queryTransfer_page.get_error_prompt_element().get_attribute('text')
        print('温馨提示10：', error_prompt)
        self.queryTransfer_handle.click_error_prompt_confirm_button()
        # 返回转账页面
        self.queryTransfer_handle.click_left_head_button_button()
        # 返回到移动银行主页面
        self.queryTransfer_handle.click_left_head_button_button()
        return error_prompt

    def query_transferG_drawpassword_excess(self):
        '''
        用例编号：111CZSX034，所有功能-查询转账-快速转账
        测试点：输入超过6位的密码，步骤：输入超过6位的密码，点击提交
        预期结果：无法输入，最多输入到6位
        :return:
        '''
        # 选择操作清单
        self.query_transferG_select()
        # 转账页面
        self.public_method.swipe_on('up', 10000)
        transfer_amount = self.read_excel.get_cell(39, 11)
        print('transfer_amount:', transfer_amount)
        self.queryTransfer_handle.send_transfer_amount_code(transfer_amount)
        self.queryTransfer_handle.click_transfer_tips_head_button()
        self.queryTransfer_handle.click_submit_transfer_button()
        # 验证码和取款密码输入页面
        self.public_method.swipe_on('up', 10000)
        self.queryTransfer_handle.click_get_code_button()
        self.queryTransfer_handle.send_input_code_code()
        self.queryTransfer_handle.click_draw_password_button()
        draw_password = self.read_excel.get_cell(39, 7)
        print('draw_password:', draw_password)
        self.queryTransfer_handle.send_draw_password_code(draw_password)
        self.queryTransfer_handle.click_input_code_code()  # 在输入取款密码后，银行自带键盘会挡住“转账”按钮
        self.queryTransfer_handle.click_transfer_account_submit_button()

        # 取温馨提示属性，再返回
        element_exist = self.queryTransfer_page.get_fail_title_element()
        print('温馨提示11：', element_exist)
        if element_exist:
            self.queryTransfer_handle.click_error_prompt_confirm_button()
            for i in range(2):
                # 返回转账页面
                # 返回到移动银行主页面
                self.queryTransfer_handle.click_left_head_button_button()
        return element_exist

    def query_transferG_bank_list(self):
        '''
        用例编号：111CZSX035，所有功能-查询转账-快速转账
        测试点：银行列表，步骤：在快速转账里点击“银行名称”
        预期结果：进入银行列表
        :return:
        '''
        # 选择操作清单
        self.queryTransfer_handle.click_action_list_button('//*[contains(@text,"查询转账")]')
        self.queryTransfer_handle.click_payee_message_button()
        self.queryTransfer_handle.click_transfer_other_button()
        self.queryTransfer_handle.click_transfer_bank_name_button()

        # 取温馨提示属性，再返回
        element_exist = self.queryTransfer_page.get_bank_list_element().is_enabled()
        # self.driver.find_element_by_id('com.gdnybank.m:id/lv_bank_list')
        print('银行列表元素存在：', element_exist)
        if element_exist:
            for i in range(3):
                # 返回收款人信息页面
                # 返回转账页面
                # 返回到移动银行主页面
                self.queryTransfer_handle.click_left_head_button_button()
        return element_exist

    def query_transferG_bank_search(self):
        '''
        用例编号：111CZSX036，所有功能-查询转账-快速转账
        测试点：搜索银行名称，步骤：在银行列表搜索栏里输入银行名称，点击搜索
        预期结果：能搜索出该银行（支持模糊搜索）
        :return:
        '''
        # 选择操作清单
        self.queryTransfer_handle.click_action_list_button('//*[contains(@text,"查询转账")]')
        self.queryTransfer_handle.click_payee_message_button()
        self.queryTransfer_handle.click_transfer_other_button()
        self.queryTransfer_handle.click_transfer_bank_name_button()
        search_bank = self.read_excel.get_cell(41, 13)
        print('search_bank:', search_bank)
        self.queryTransfer_handle.send_search_bank_code(search_bank)
        self.queryTransfer_handle.click_search_button_button()

        # 取温馨提示属性，再返回
        search_bank_element = self.read_excel.get_cell(41, 14)
        print('search_bank_element:', search_bank_element)
        element_exist = self.queryTransfer_page.get_bank_list_element().find_element_by_xpath(search_bank_element)
        print('获取银行元素：', element_exist)
        if element_exist:
            for i in range(3):
                # 返回收款人信息页面
                # 返回转账页面
                # 返回到移动银行主页面
                self.queryTransfer_handle.click_left_head_button_button()
        return element_exist

    def query_transferG_payee_list(self):
        '''
        用例编号：111CZSX037，所有功能-查询转账-快速转账
        测试点：收款人名册，步骤：进入快速转账，点击账户姓名右侧的图标
        预期结果：进入收款人列表，列表内显示进行过交易的收款人信息
        :return:
        '''
        # 选择操作清单
        self.queryTransfer_handle.click_action_list_button('//*[contains(@text,"查询转账")]')
        self.queryTransfer_handle.click_payee_message_button()
        self.queryTransfer_handle.click_transfer_other_button()
        self.queryTransfer_handle.click_transfer_payee_head_button()

        # 取温馨提示属性，再返回
        # 取的是收款人列表的银行卡号元素
        element_exist = self.queryTransfer_page.get_bank_list_card_element()
        print('获取收款人列表元素：', element_exist)
        if element_exist:
            if element_exist:
                for i in range(3):
                    # 返回收款人信息页面
                    # 返回转账页面
                    # 返回到移动银行主页面
                    self.queryTransfer_handle.click_left_head_button_button()
        return element_exist

    def query_transferG_payee_choice(self):
        '''
        用例编号：111CZSX038，所有功能-查询转账-快速转账
        测试点：选择收款人，步骤：在收款人列表，点击其中一个收款人信息
        预期结果：自动返回上一页面，且账户姓名、收款人账号、银行名称已自动填写为选择的收款人信息
        :return:
        '''
        # 选择操作清单
        self.queryTransfer_handle.click_action_list_button('//*[contains(@text,"查询转账")]')
        self.queryTransfer_handle.click_payee_message_button()
        self.queryTransfer_handle.click_transfer_other_button()
        self.queryTransfer_handle.click_transfer_payee_head_button()

        # 选择收款人页面列表，具体的收款人在excel维护
        payee_name = self.read_excel.get_cell(43, 8)
        print('payee_name:', payee_name)
        self.queryTransfer_handle.click_bank_list_list(payee_name)
        # driver.find_elements_by_class_name("android.wdget.RelativeLayout").__getitem__(1).click()

        # 返回到收款人信息页面，取的是收款人账号元素
        element_code = self.queryTransfer_page.get_payee_account_element().get_attribute("text")
        # self.driver.find_element_by_id('com.gdnybank.m:id/tv_card_num')
        print('获取到的元素：', element_code)
        element_length = len(element_code)
        print('元素长度：', element_length)
        element_compare = (element_length > 8)  # 考虑到还没输入账号时，是5位字符，账号可能至少有8位
        if element_compare:
            for i in range(2):
                # 返回转账页面
                # 返回到移动银行主页面
                self.queryTransfer_handle.click_left_head_button_button()
        return element_compare

    def query_transferG_payee_add(self):
        '''
        用例编号：111CZSX039，所有功能-查询转账-快速转账
        测试点：添加收款人，步骤：进行一笔快速转账交易
        预期结果：交易成功后自动将该收款人添加进收款人名册
        :return: payeelist_compare
        '''

        # 选择操作清单
        self.queryTransfer_handle.click_action_list_button('//*[contains(@text,"查询转账")]')
        self.queryTransfer_handle.click_payee_message_button()
        self.queryTransfer_handle.click_transfer_other_button()
        self.queryTransfer_handle.click_transfer_payee_head_button()

        # 添加收款人前的收款人清单数量
        # payeelist_before = self.queryTransfer_page.get_bank_list_card_element()
        # print('添加前元素：' ,payeelist_before)
        payeelist_length_before = len(self.queryTransfer_page.get_bank_list_card_element())
        print('添加前：', payeelist_length_before)

        # 返回转账页面
        self.queryTransfer_handle.click_left_head_button_button()
        payee_name = self.read_excel.get_cell(44, 8)
        print('payee_name:', payee_name)
        self.queryTransfer_handle.send_payee_name_code(payee_name)

        # 判断当所输入账号与预期的不一致时，则输入，否则继续下一步选择银行名称
        payee_account = self.read_excel.get_cell(44, 9)
        print('payee_account:', payee_account)
        payee_account_after = 1
        while payee_account != payee_account_after:
            # payee_account = '6235 9574 0000 6141 031'
            # 清除
            self.queryTransfer_handle.clear_payee_account_code()
            time.sleep(5)
            # 输入银行账号
            input_element = self.queryTransfer_page.get_payee_account_element()
            input_element.click()
            self.press_Keycode.press_Keycode(payee_account, input_element)

            # self.queryTransfer_handle.send_payee_account_code(payee_account)
            # 获取输入后的银行账号
            time.sleep(2)

            payee_account_after_original = self.queryTransfer_page.get_payee_input_element()[1].get_attribute("text")
            # print('payee_account_after_original:', payee_account_after_original)
            payee_account_after = "".join(payee_account_after_original.split())  # 将输入后的银行卡号空格去掉再对比结果
            print('输入后银行账号：', payee_account_after)

        self.queryTransfer_handle.click_transfer_bank_name_button()
        time.sleep(2)
        payee_bank = self.read_excel.get_cell(44, 10)
        print('payee_bank:', payee_bank)
        self.queryTransfer_handle.click_bank_list_list(payee_bank)
        time.sleep(2)
        self.queryTransfer_handle.click_submit_transfer_button()
        time.sleep(2)
        # 调用转账页面方法
        self.query_transfer_page(44, 11, 44, 7, 44, 12) # 更新转账数据

        # 选择操作清单
        self.queryTransfer_handle.click_action_list_button('//*[contains(@text,"查询转账")]')
        self.queryTransfer_handle.click_payee_message_button()
        self.queryTransfer_handle.click_transfer_other_button()
        self.queryTransfer_handle.click_transfer_payee_head_button()

        # 添加新的收款人后的收款人清单数量
        # payeelist_after = self.queryTransfer_page.get_bank_list_card_element()
        payeelist_length_after = len(self.queryTransfer_page.get_bank_list_card_element())
        print('添加后：', payeelist_length_after)
        payeelist_compare = (payeelist_length_before < payeelist_length_after)
        print('对比结果：', payeelist_compare)
        if payeelist_compare:
            for i in range(3):
                # 返回收款人信息页面
                # 返回转账页面
                # 返回到移动银行主页面
                self.queryTransfer_handle.click_left_head_button_button()

        keyword = '确认'
        confirm = '确认'
        while keyword in confirm:
            confirm_element = self.queryTransfer_page.get_error_confirm_element()
            # print('confirm_element:', confirm_element)
            confirm = confirm_element[0].get_attribute('text')
            # print('弹框信息关键词：', confirm)
            confirm_element[0].click()

        return payeelist_compare

    def query_transferG_payee_delete_before(self):
        '''
        用例编号：111CZSX040，所有功能-查询转账-快速转账
        测试点：删除收款人，步骤：在收款人列表，点击右上角编辑，然后点击某收款人左侧删除按钮
        预期结果：成功删除该收款人信息
        本方法是记录删除前得到需要删除的选项，返回i
        :return: i
        '''
        # 选择操作清单
        self.queryTransfer_handle.click_action_list_button('//*[contains(@text,"查询转账")]')
        self.queryTransfer_handle.click_payee_message_button()
        self.queryTransfer_handle.click_transfer_other_button()
        self.queryTransfer_handle.click_transfer_payee_head_button()

        self.queryTransfer_handle.click_payee_list_edit_button()
        # 获取要删除的收款人元素-》再获取按照银行名称查询的id定位元素-》for再while语句判断删除收款人元素排在第几位，得到i+1
        # 最后使用删除按钮find_elements_by_id('删除id')[i+1].click()
        payee_name_target = self.read_excel.get_cell(45, 15)
        print('payee_name_target:', payee_name_target)

        # targets_element = self.driver.find_elements_by_id('com.gdnybank.m:id/tv_name_payee_contant_item')
        targets_element = self.queryTransfer_page.get_payee_list_name_element()
        # print('收款人列表元素：' ,targets_element)
        targets_element_length = len(targets_element)
        print('收款人列表元素长度：', targets_element_length)
        for i in range(targets_element_length):
            payee_name = targets_element[i].get_attribute('text')
            print('第' + str(i) + '收款人名字：', payee_name)
            if payee_name_target == payee_name:
                print('收款人元素数组：', i)
                return i

    def query_transferG_payee_delete(self):
        '''
        用例编号：111CZSX040，所有功能-查询转账-快速转账
        测试点：删除收款人，步骤：在收款人列表，点击右上角编辑，然后点击某收款人左侧删除按钮
        预期结果：成功删除该收款人信息
        :return: payeelist_compare_length
        '''
        # 调用删除前需要删除的元素第几位元素
        j = self.query_transferG_payee_delete_before()
        print('取到值：', j)
        # 删除收款人前的收款人清单数量
        payeelist_length_before = len(self.queryTransfer_page.get_bank_list_card_element())
        print('删除前长度：', payeelist_length_before)
        # delete_element = self.driver.find_elements_by_id('com.gdnybank.m:id/btn_del_payee_contact_item')[j]
        delete_element = self.queryTransfer_page.get_payee_delete_element()[j]
        delete_element.click()
        # self.queryTransfer_handle.click_payee_delete_button()
        payeelist_length_after = len(self.queryTransfer_page.get_bank_list_card_element())
        print('删除后长度：', payeelist_length_after)
        payeelist_compare = (payeelist_length_before > payeelist_length_after)
        print('对比结果：', payeelist_compare)
        if payeelist_compare:
            self.queryTransfer_handle.click_payee_list_complete_button()
            for i in range(3):
                # 返回收款人信息页面
                # 返回转账页面
                # 返回到移动银行主页面
                self.queryTransfer_handle.click_left_head_button_button()
        return payeelist_compare

    def query_transferG_payee_cityChoice(self):
        '''
        用例编号：111CZSX041，所有功能-查询转账-快速转账
        测试点：收款支行选择，步骤：点击银行名称进入银行列表，点击某其他银行
        预期结果：进入支行选择页面
        :return:
        '''
        # 选择操作清单
        self.queryTransfer_handle.click_action_list_button('//*[contains(@text,"查询转账")]')
        self.queryTransfer_handle.click_payee_message_button()
        self.queryTransfer_handle.click_transfer_other_button()
        # self.queryTransfer_handle.click_transfer_payee_head_button()

        self.queryTransfer_handle.click_transfer_bank_name_button()
        payee_bank = self.read_excel.get_cell(46, 13)
        print('payee_bank:', payee_bank)
        self.queryTransfer_handle.click_bank_list_list(payee_bank)
        # 进入南粤银行以外的银行，显示支行信息
        # 获取支行页面的关键字来验证
        self.queryTransfer_handle.click_search_city_button()
        # 如果选择非广州的城市，则需要先查询，但如果是热门城市，搜索再选择，会有两个搜索结果
        # self.queryTransfer_handle.send_search_city_code('广州')
        # self.queryTransfer_handle.click_city_branch_search_button()
        # 可能是find_elements
        city = self.read_excel.get_cell(46, 16)
        print('city:', city)
        # citys_element = self.driver.find_elements_by_id('com.gdnybank.m:id/city')
        citys_element = self.queryTransfer_page.get_city_list_element()
        # print('城市列表元素：' ,citys_element)
        citys_element_length = len(citys_element)
        print('城市列表元素长度：', citys_element_length)
        for i in range(citys_element_length):
            city_name = citys_element[i].get_attribute('text')
            print('第' + str(i) + '城市：', city_name)
            if city == city_name:
                # print('城市元素数组：', i)
                return i

    def query_transferG_payee_branch(self):
        '''
        用例编号：111CZSX041，所有功能-查询转账-快速转账
        测试点：收款支行选择，步骤：点击银行名称进入银行列表，点击某其他银行
        预期结果：进入支行选择页面
        :return:
        '''
        # 调用查看前需要搜索城市在第几位元素
        j = self.query_transferG_payee_cityChoice()
        # print('城市元素取到值：',j)
        city_elements = self.queryTransfer_page.get_city_list_element()[j]
        city_elements.click()
        self.queryTransfer_handle.click_branch_search_button()
        branch_amount = self.queryTransfer_page.get_branch_bank_amount_element().get_attribute('text')
        print('获取的属性：', branch_amount)
        branch_amountRe = re.sub("\D", "", branch_amount)
        print('抽取出来的数字有：', branch_amountRe)
        compare_branch_amount = branch_amountRe > '0'
        if compare_branch_amount:
            for i in range(4):
                self.queryTransfer_handle.click_left_head_button_button()
        return compare_branch_amount

    def query_transferG_payee_city(self):
        '''
        用例编号：111CZSX042，所有功能-查询转账-快速转账
        测试点：选择转入账号城市，步骤：点击城市名称搜索栏
        预期结果：弹出城市列表
        :return:
        '''
        # 选择操作清单
        self.queryTransfer_handle.click_action_list_button('//*[contains(@text,"查询转账")]')
        self.queryTransfer_handle.click_payee_message_button()
        self.queryTransfer_handle.click_transfer_other_button()
        # self.queryTransfer_handle.click_transfer_payee_head_button()

        self.queryTransfer_handle.click_transfer_bank_name_button()
        payee_bank = self.read_excel.get_cell(47, 13)
        print('payee_bank:', payee_bank)
        self.queryTransfer_handle.click_bank_list_list(payee_bank)
        # 进入南粤银行以外的银行，显示支行信息
        # 获取支行页面的关键字来验证

        self.queryTransfer_handle.click_search_city_button()
        verify_title = '城市列表'
        city_list = self.queryTransfer_page.get_title_head_element().get_attribute('text')
        print('获取到的头条标题：', city_list)
        city_compare = (city_list == verify_title)
        print('城市列表对比结果：', city_compare)
        if city_list == verify_title:
            for i in range(5):
                self.queryTransfer_handle.click_left_head_button_button()
        return city_list

    def query_transferG_branch_keyword(self):
        '''
        用例编号：111CZSX043，所有功能-查询转账-快速转账
        测试点：支行关键字搜索，步骤：选择城市后，输入关键字进行搜索
        预期结果：成功搜索出该城市下有该关键字的支行
        :return:
        '''
        # 调用查看前需要搜索城市在第几位元素
        j = self.query_transferG_payee_cityChoice()
        print('城市元素取到值：', j)
        city_elements = self.queryTransfer_page.get_city_list_element()[j]
        city_elements.click()
        self.queryTransfer_handle.click_branch_search_button()
        time.sleep(5)
        branch_amount = self.queryTransfer_page.get_branch_bank_amount_element().get_attribute('text')
        print('获取的属性：', branch_amount)
        branch_amountRe = re.sub("\D", "", branch_amount)
        print('抽取出来的数字有：', branch_amountRe)
        compare_branch_amount = branch_amountRe > '0'
        if compare_branch_amount:
            print('查询分行信息正常')
        branchKeyword = self.read_excel.get_cell(48, 17)
        self.queryTransfer_handle.send_branch_keyword_code(branchKeyword)
        self.queryTransfer_handle.click_branch_search_button()
        branch_bank = self.queryTransfer_page.get_branch_bank_keyword_element()
        print('分行查询结果元素：', branch_bank)
        if branch_bank != None:
            for i in range(4):
                self.queryTransfer_handle.click_left_head_button_button()
        return branch_bank

    def query_transferG_account_detail(self):
        '''
        用例编号：111CZSX044，所有功能-查询转账-快速转账
        测试点：查看账户详情，步骤：点击卡片右下角的感叹号
        预期结果：进入对应账户的详情页面
        :return:
        '''
        # 选择操作清单
        self.queryTransfer_handle.click_action_list_button('//*[contains(@text,"查询转账")]')
        time.sleep(2)
        self.queryTransfer_handle.click_account_plaint_button()
        # 获取账户详情的元素
        # 再打印账户详情的信息点到excel
        account_amount = len(self.queryTransfer_page.get_account_types_element())
        print('账户种类：', account_amount)
        account_message = []
        if account_amount > 0:
            for i in range(account_amount):
                account_types = self.queryTransfer_page.get_account_types_element()
                account_balances = self.queryTransfer_page.get_account_balance_element()
                regist_dates = self.queryTransfer_page.get_regist_date_element()
                acc_type = "acc_type" + str(i)
                account_balance = "account_balance" + str(i)
                regist_date = "regist_date" + str(i)
                print('赋值：', acc_type, ",", account_balance, ",", regist_date)
                acc_type = account_types[i].get_attribute('text')
                account_balance = account_balances[i].get_attribute('text')
                regist_date = regist_dates[i].get_attribute('text')
                account_message.append(acc_type)
                account_message.append(account_balance)
                account_message.append(regist_date)
                print('第' + str(i) + '账户种类：', acc_type)
                print('第' + str(i) + '账户余额：', account_balance)
                print('第' + str(i) + '开户日期：', regist_date)
                print('列表：', account_message)
                # self.write_excel.write(27, 18, account_message)
            print('列表account_message：', account_message)
            account_message_str = ",".join(account_message)
            print('列表转换为字符串：', account_message_str)
            self.write_excel.write(27, 18, account_message_str)

            for j in range(2):
                self.queryTransfer_handle.click_left_head_button_button()
        else:
            return None
        return account_amount

#--------------------------------------------查询转账->次日转账------------------------------------------------------
    '''
    查询转账->次日转账
    '''

    def query_transferT_select(self):
        '''
        用例编号：111CZSX039,所有功能-查询转账-快速转账
        同行转账-正确输入金额-》步骤：进入快速转账，输入收款人姓名、账号，在银行列表选择同行进行转账，转账金额在（0，余额]之内
        query_transfer_select：从收款人列表中选择账户来转账
        :return:
        '''
        # 选择操作清单
        self.queryTransfer_handle.click_action_list_button('//*[contains(@text,"查询转账")]')
        self.queryTransfer_handle.click_payee_message_button()
        self.queryTransfer_handle.click_transfer_other_button()
        self.queryTransfer_handle.click_transfer_tomorrow_button()
        # 选择账户姓名编辑框右侧的头像按钮
        self.queryTransfer_handle.click_transfer_payee_head_button()
        # 收款人信息页面
        payee_name = self.read_excel.get_cell(50, 8)
        print('payee_name:', payee_name)
        self.queryTransfer_handle.click_bank_list_list(payee_name)
        time.sleep(2)
        self.queryTransfer_handle.click_submit_transfer_button()
        time.sleep(2)

        # # 调用转账页面方法
        # self.query_transfer_page(50, 11, 50, 7, 50, 12) # 更新转账数据


    def query_transferT_amount_zero(self):
        '''
        用例编号：111CZSX024,所有功能-查询转账-快速转账
        测试点：同行转账-金额为0，步骤：转账金额为0，预期结果：温馨提示：转账金额输入有误
        :return:
        '''
        # 选择操作清单
        self.query_transferG_select()
        # 转账页面
        self.public_method.swipe_on('up', 10000)
        transfer_amount = self.read_excel.get_cell(52, 11)
        print('transfer_amount:', transfer_amount)
        self.queryTransfer_handle.send_transfer_amount_code(transfer_amount)
        self.queryTransfer_handle.click_transfer_tips_head_button()
        self.queryTransfer_handle.click_submit_transfer_button()
        # 取温馨提示属性，再返回
        error_prompt = self.queryTransfer_page.get_error_prompt_element().get_attribute('text')
        print('温馨提示2：', error_prompt)
        self.queryTransfer_handle.click_error_prompt_confirm_button()
        # 返回到移动银行主页面
        self.queryTransfer_handle.click_left_head_button_button()
        return error_prompt

    def query_transferT_beyond_balance(self):
        '''
        用例编号：111CZSX025,所有功能-查询转账-快速转账
        测试点：同行转账-超出余额，步骤：转账金额大于可用余额，预期结果：温馨提示：余额不足
        :return:
        '''
        # 选择操作清单
        self.query_transferG_select()
        # 转账页面
        self.public_method.swipe_on('up', 10000)
        transfer_amount = self.read_excel.get_cell(53, 11)
        print('transfer_amount:', transfer_amount)
        self.queryTransfer_handle.send_transfer_amount_code(transfer_amount)
        self.queryTransfer_handle.click_transfer_tips_head_button()
        self.queryTransfer_handle.click_submit_transfer_button()
        # 取温馨提示属性，再返回
        error_prompt = self.queryTransfer_page.get_error_prompt_element().get_attribute('text')
        print('温馨提示3：', error_prompt)
        self.queryTransfer_handle.click_error_prompt_confirm_button()
        # 返回到移动银行主页面
        self.queryTransfer_handle.click_left_head_button_button()
        return error_prompt

    def query_transferT_amount_space(self):
        '''
        用例编号：111CZSX026,所有功能-查询转账-快速转账
        测试点：同行转账-金额不填，步骤：转账金额留空不填，预期结果：温馨提示：请输入转账金额
        :return:
        '''
        # 选择操作清单
        self.query_transferG_select()
        # 转账页面
        self.public_method.swipe_on('up', 10000)
        self.queryTransfer_handle.click_transfer_tips_head_button()
        self.queryTransfer_handle.click_submit_transfer_button()
        # 取温馨提示属性，再返回
        error_prompt = self.queryTransfer_page.get_error_prompt_element().get_attribute('text')
        print('温馨提示4：', error_prompt)
        self.queryTransfer_handle.click_error_prompt_confirm_button()
        # 返回到移动银行主页面
        self.queryTransfer_handle.click_left_head_button_button()
        return error_prompt

    def query_transferT_amount_capital(self):
        '''
        用例编号：111CZSX027,所有功能-查询转账-快速转账
        测试点：同行转账-大写金额，步骤：输入金额后查看大写金额，预期结果：显示正确
        :return:
        '''
        # 选择操作清单
        self.query_transferG_select()
        # 转账页面
        self.public_method.swipe_on('up', 10000)
        transfer_amount = self.read_excel.get_cell(55, 11)
        print('transfer_amount:', transfer_amount)
        self.queryTransfer_handle.send_transfer_amount_code(transfer_amount)
        self.queryTransfer_handle.click_transfer_tips_head_button()
        self.queryTransfer_handle.click_submit_transfer_button()
        # 取温馨提示属性，再返回
        error_prompt = self.queryTransfer_page.get_error_prompt_element().get_attribute('text')
        print('温馨提示5：', error_prompt)
        self.queryTransfer_handle.click_error_prompt_confirm_button()
        # 返回到移动银行主页面
        self.queryTransfer_handle.click_left_head_button_button()
        return error_prompt

    def query_transferT_payee_wrong(self):
        '''
        用例编号：111CZSX028,所有功能-查询转账-快速转账
        测试点：同行转账-收方信息错误，步骤：进入快速转账，输入收款账号，收款人姓名，开户行三者的任意不匹配，
        预期结果：系统提示：账户和户名不匹配
        :return:error_prompt
        '''
        # 选择操作清单
        self.queryTransfer_handle.click_action_list_button('//*[contains(@text,"查询转账")]')
        self.queryTransfer_handle.click_payee_message_button()
        self.queryTransfer_handle.click_transfer_other_button()
        self.queryTransfer_handle.click_transfer_tomorrow_button()
        # 收款人信息页面,输入错误的收款名
        payee_name = self.read_excel.get_cell(56, 8)
        print('payee_name:', payee_name)
        self.queryTransfer_handle.send_payee_name_code(payee_name)
        # 判断当所输入账号与预期的不一致时，则输入，否则继续下一步选择银行名称
        payee_account = self.read_excel.get_cell(56, 9)
        print('payee_account:', payee_account)
        payee_account_after = 1
        while payee_account != payee_account_after:
            # payee_account = '6235 9574 0000 6141 031'
            # 清除
            self.queryTransfer_handle.clear_payee_account_code()
            time.sleep(5)
            # 输入银行账号
            input_element = self.queryTransfer_page.get_payee_account_element()
            input_element.click()
            self.press_Keycode.press_Keycode(payee_account, input_element)

            # self.queryTransfer_handle.send_payee_account_code(payee_account)
            # 获取输入后的银行账号
            time.sleep(2)

            payee_account_after_original = self.queryTransfer_page.get_payee_input_element()[1].get_attribute("text")
            payee_account_after = "".join(payee_account_after_original.split())  # 将输入后的银行卡号空格去掉再对比结果
            print('输入后银行账号：', payee_account_after)

        self.queryTransfer_handle.click_transfer_bank_name_button()
        time.sleep(2)
        payee_bank = self.read_excel.get_cell(56, 10)
        print('payee_name:', payee_bank)
        self.queryTransfer_handle.click_bank_list_list(payee_bank)
        time.sleep(2)
        self.queryTransfer_handle.click_submit_transfer_button()
        time.sleep(2)
        # 转账页面
        transfer_amount = self.read_excel.get_cell(56, 11)
        print('transfer_amount:', transfer_amount)
        self.queryTransfer_handle.send_transfer_amount_code(transfer_amount)
        self.public_method.swipe_on('up', 10000)
        self.queryTransfer_handle.click_transfer_tips_head_button()
        self.queryTransfer_handle.click_submit_transfer_button()
        # 取温馨提示属性，再返回
        error_prompt = self.queryTransfer_page.get_error_prompt_element().get_attribute('text')
        print('温馨提示6：', error_prompt)
        self.queryTransfer_handle.click_error_prompt_confirm_button()
        # 返回到移动银行主页面
        self.queryTransfer_handle.click_left_head_button_button()
        return error_prompt

    def query_transferT_payee_space(self):
        '''
        用例编号：111CZSX023,所有功能-查询转账-快速转账
        测试点：同行转账-收款人不填，步骤：收款人信息留空不填，预期结果：温馨提示：请输入收款人信息
        :return:
        '''

        # 选择操作清单
        # print('read_excel方法query_transferF_payee_space:', self.read_excel)
        self.queryTransfer_handle.click_action_list_button('//*[contains(@text,"查询转账")]')
        self.queryTransfer_handle.click_payee_message_button()
        self.queryTransfer_handle.click_transfer_other_button()
        self.queryTransfer_handle.click_transfer_tomorrow_button()
        # 不输入收款人信息，直接点击提交按钮
        time.sleep(2)
        self.queryTransfer_handle.click_submit_transfer_button()
        # 取温馨提示属性，再返回
        error_prompt = self.queryTransfer_page.get_error_prompt_element().get_attribute('text')
        print('温馨提示1：' ,error_prompt)
        self.queryTransfer_handle.click_error_prompt_confirm_button()
        # 返回到转账页面
        self.queryTransfer_handle.click_left_head_button_button()
        # 返回到移动银行主页面
        self.queryTransfer_handle.click_left_head_button_button()
        return error_prompt

    def query_transferT_same_payer(self):
        '''
        用例编号：111CZSX029,所有功能-查询转账-快速转账
        测试点：同账户转账，步骤：进入快速转账，收款人与付款人为同一人
        预期结果：系统提示：转入转出账户不能相同
        :return:error_prompt
        '''
        # 选择操作清单
        self.queryTransfer_handle.click_action_list_button('//*[contains(@text,"查询转账")]')
        self.queryTransfer_handle.click_payee_message_button()
        self.queryTransfer_handle.click_transfer_other_button()
        self.queryTransfer_handle.click_transfer_tomorrow_button()
        payee_name = self.read_excel.get_cell(57, 8)
        print('payee_name:', payee_name)
        self.queryTransfer_handle.send_payee_name_code(payee_name)
        # 判断当所输入账号与预期的不一致时，则输入，否则继续下一步选择银行名称
        payee_account = self.read_excel.get_cell(57, 9)
        print('payee_account:', payee_account)
        payee_account_after = 1
        while payee_account != payee_account_after:
            # payee_account = '6235 9574 0000 6141 031'
            # 清除
            self.queryTransfer_handle.clear_payee_account_code()
            time.sleep(5)
            # 输入银行账号
            input_element = self.queryTransfer_page.get_payee_account_element()
            input_element.click()
            self.press_Keycode.press_Keycode(payee_account, input_element)

            # self.queryTransfer_handle.send_payee_account_code(payee_account)
            # 获取输入后的银行账号
            time.sleep(2)

            payee_account_after_original = self.queryTransfer_page.get_payee_input_element()[1].get_attribute("text")
            # print('payee_account_after_original:', payee_account_after_original)
            payee_account_after = "".join(payee_account_after_original.split())  # 将输入后的银行卡号空格去掉再对比结果
            print('输入后银行账号：', payee_account_after)

        self.queryTransfer_handle.click_transfer_bank_name_button()
        time.sleep(2)
        payee_bank = self.read_excel.get_cell(57,10)
        print('payee_bank:', payee_bank)
        self.queryTransfer_handle.click_bank_list_list(payee_bank)
        time.sleep(2)
        self.queryTransfer_handle.click_submit_transfer_button()
        time.sleep(2)
        # 转账页面
        transfer_amount = self.read_excel.get_cell(57, 11)
        print('transfer_amount:', transfer_amount)
        self.queryTransfer_handle.send_transfer_amount_code(transfer_amount)
        self.public_method.swipe_on('up', 10000)
        self.queryTransfer_handle.click_transfer_tips_head_button()
        self.queryTransfer_handle.click_submit_transfer_button()
        # 取温馨提示属性，再返回
        error_prompt = self.queryTransfer_page.get_error_prompt_element().get_attribute('text')
        print('温馨提示7：', error_prompt)
        self.queryTransfer_handle.click_error_prompt_confirm_button()
        # 返回到移动银行主页面
        self.queryTransfer_handle.click_left_head_button_button()
        return error_prompt

    def query_transferT_drawpassword_wrong(self):
        '''
        用例编号：111CZSX030，所有功能-查询转账-快速转账
        测试点：密码输入错误，步骤：输入错误密码后提交，预期结果：系统提示：您已输错密码[n]次，再输错[3-n]次，将锁定手机盾
        :return:error_prompt
        '''
        # 选择操作清单
        self.query_transferT_select()
        # 转账页面
        self.public_method.swipe_on('up', 10000)
        transfer_amount = self.read_excel.get_cell(58, 11)
        print('transfer_amount:', transfer_amount)
        self.queryTransfer_handle.send_transfer_amount_code(transfer_amount)
        self.queryTransfer_handle.click_transfer_tips_head_button()
        self.queryTransfer_handle.click_submit_transfer_button()
        # 验证码和取款密码输入页面
        self.public_method.swipe_on('up', 10000)
        self.queryTransfer_handle.click_get_code_button()
        self.queryTransfer_handle.send_input_code_code()
        self.queryTransfer_handle.click_draw_password_button()
        draw_password = self.read_excel.get_cell(58, 7)
        print('draw_password:', draw_password)
        self.queryTransfer_handle.send_draw_password_code(draw_password)
        self.queryTransfer_handle.click_input_code_code()  # 在输入取款密码后，银行自带键盘会挡住“转账”按钮
        self.queryTransfer_handle.click_transfer_account_submit_button()
        # 取温馨提示属性，再返回
        error_prompt = self.queryTransfer_page.get_error_prompt_element().get_attribute('text')
        print('温馨提示8：', error_prompt)
        self.queryTransfer_handle.click_error_prompt_confirm_button()
        for i in range(2):
            # 返回转账页面
            # 返回到移动银行主页面
            self.queryTransfer_handle.click_left_head_button_button()
        return error_prompt

    def query_transferT_drawpassword_again(self):
        '''
        用例编号：111CZSX031，所有功能-查询转账-快速转账
        测试点：密码输入错误，再输入正确，步骤：输入错误密码次数小于3次，再输入正确密码，点击提交，
        预期结果：成功提交，并且错误次数重置
        :return:transfer_submitted_mark
        '''
        # 取款密码错误
        self.query_transferT_drawpassword_wrong()
        # 取款密码错误后，再次输入正常密码
        self.query_transferT_select()

        # 转账页面
        self.public_method.swipe_on('up', 10000)
        transfer_amount = self.read_excel.get_cell(59, 11)
        print('transfer_amount:', transfer_amount)
        self.queryTransfer_handle.send_transfer_amount_code(transfer_amount)
        self.queryTransfer_handle.click_transfer_tips_head_button()
        self.queryTransfer_handle.click_submit_transfer_button()

        # 转账输入验证码和取款密码页面
        self.public_method.swipe_on('up', 10000)
        self.queryTransfer_handle.click_get_code_button()
        self.queryTransfer_handle.send_input_code_code()
        self.queryTransfer_handle.click_draw_password_button()
        draw_password = self.read_excel.get_cell(59, 7)
        print('draw_password:', draw_password)
        self.queryTransfer_handle.send_draw_password_code(draw_password)
        self.queryTransfer_handle.click_input_code_code()  # 在输入取款密码后，银行自带键盘会挡住“转账”按钮
        self.queryTransfer_handle.click_transfer_account_submit_button()

        # 转账成功页面
        time.sleep(3)
        transfer_submitted_mark = self.queryTransfer_page.get_transfer_submitted_element().get_attribute("text")
        print('转账成功提示：', transfer_submitted_mark)
        # time.sleep(3)
        # remaining_balance = self.queryTransfer_page.get_error_prompt_element().get_attribute('text')
        # print('余额：', remaining_balance)
        # self.write_excel.write(59, 12, remaining_balance)
        self.queryTransfer_handle.click_inform_success_button()  # 点击“好，我知道了”按钮后，跳转到移动银行主页

        keyword = '确认'
        confirm = '确认'
        while keyword in confirm:
            confirm_element = self.queryTransfer_page.get_error_confirm_element()
            # print('confirm_element:', confirm_element)
            confirm = confirm_element[0].get_attribute('text')
            # print('弹框信息关键词：', confirm)
            confirm_element[0].click()
        return transfer_submitted_mark

    def query_transferT_drawpassword_lock(self):
        '''
        用例编号：111CZSX032，所有功能-查询转账-快速转账
        测试点：密码输入错误达到5次锁定，步骤：输入错误密码次数达到3次，点击提交
        预期结果：系统提示：已锁定
        :return:
        '''
        # 选择操作清单
        self.query_transferG_select()
        # 转账页面
        self.public_method.swipe_on('up', 10000)
        transfer_amount = self.read_excel.get_cell(14, 10)
        print('transfer_amount:', transfer_amount)
        self.queryTransfer_handle.send_transfer_amount_code(transfer_amount)
        self.queryTransfer_handle.click_transfer_tips_head_button()
        self.queryTransfer_handle.click_submit_transfer_button()
        # 验证码和取款密码输入页面
        self.public_method.swipe_on('up', 10000)
        self.queryTransfer_handle.click_get_code_button()
        self.queryTransfer_handle.send_input_code_code()
        self.queryTransfer_handle.click_draw_password_button()
        # 输入取款密码错误3次，则锁卡
        for i in range(3):
            draw_password = self.read_excel.get_cell(14, 6)
            print('draw_password:', draw_password)
            self.queryTransfer_handle.send_draw_password_code(draw_password)
            self.queryTransfer_handle.click_input_code_code()  # 在输入取款密码后，银行自带键盘会挡住“转账”按钮
            self.queryTransfer_handle.click_transfer_account_submit_button()
            # 取温馨提示属性，再返回
            error_prompt = self.driver.find_element_by_id('com.gdnybank.m:id/tv_metion_msg').get_attribute('text')
            print('温馨提示9：', error_prompt)
            self.queryTransfer_handle.click_error_prompt_confirm_button()
            return error_prompt
        # 返回转账页面
        self.queryTransfer_handle.click_left_head_button_button()
        # 返回到移动银行主页面
        self.queryTransfer_handle.click_left_head_button_button()
        # return error_prompt

    def query_transferT_drawpassword_lack(self):
        '''
        用例编号：111CZSX033，所有功能-查询转账-快速转账
        测试点：密码输入字数不足，步骤：输入小于6位数的密码，点击提交
        预期结果：取款密码输入不正确，请重新输入
        :return:
        '''
        # 选择操作清单
        self.query_transferG_select()
        # 转账页面
        self.public_method.swipe_on('up', 10000)
        transfer_amount = self.read_excel.get_cell(60, 11)
        print('transfer_amount:', transfer_amount)
        self.queryTransfer_handle.send_transfer_amount_code(transfer_amount)
        self.queryTransfer_handle.click_transfer_tips_head_button()
        self.queryTransfer_handle.click_submit_transfer_button()
        # 验证码和取款密码输入页面
        self.public_method.swipe_on('up', 10000)
        self.queryTransfer_handle.click_get_code_button()
        self.queryTransfer_handle.send_input_code_code()
        self.queryTransfer_handle.click_draw_password_button()
        draw_password = self.read_excel.get_cell(60, 7)
        print('draw_password:', draw_password)
        self.queryTransfer_handle.send_draw_password_code(draw_password)
        self.queryTransfer_handle.click_input_code_code()  # 在输入取款密码后，银行自带键盘会挡住“转账”按钮
        self.queryTransfer_handle.click_transfer_account_submit_button()

        # 取温馨提示属性，再返回
        error_prompt = self.queryTransfer_page.get_error_prompt_element().get_attribute('text')
        print('温馨提示10：', error_prompt)
        self.queryTransfer_handle.click_error_prompt_confirm_button()
        # 返回转账页面
        self.queryTransfer_handle.click_left_head_button_button()
        # 返回到移动银行主页面
        self.queryTransfer_handle.click_left_head_button_button()
        return error_prompt

    def query_transferT_drawpassword_excess(self):
        '''
        用例编号：111CZSX034，所有功能-查询转账-快速转账
        测试点：输入超过6位的密码，步骤：输入超过6位的密码，点击提交
        预期结果：无法输入，最多输入到6位
        :return:
        '''
        # 选择操作清单
        self.query_transferG_select()
        # 转账页面
        self.public_method.swipe_on('up', 10000)
        transfer_amount = self.read_excel.get_cell(61, 11)
        print('transfer_amount:', transfer_amount)
        self.queryTransfer_handle.send_transfer_amount_code(transfer_amount)
        self.queryTransfer_handle.click_transfer_tips_head_button()
        self.queryTransfer_handle.click_submit_transfer_button()
        # 验证码和取款密码输入页面
        self.public_method.swipe_on('up', 10000)
        self.queryTransfer_handle.click_get_code_button()
        self.queryTransfer_handle.send_input_code_code()
        self.queryTransfer_handle.click_draw_password_button()
        draw_password = self.read_excel.get_cell(61, 7)
        print('draw_password:', draw_password)
        self.queryTransfer_handle.send_draw_password_code(draw_password)
        self.queryTransfer_handle.click_input_code_code()  # 在输入取款密码后，银行自带键盘会挡住“转账”按钮
        self.queryTransfer_handle.click_transfer_account_submit_button()

        # 取温馨提示属性，再返回
        element_exist = self.queryTransfer_page.get_fail_title_element()
        print('温馨提示11：', element_exist)
        if element_exist:
            self.queryTransfer_handle.click_error_prompt_confirm_button()
            for i in range(2):
                # 返回转账页面
                # 返回到移动银行主页面
                self.queryTransfer_handle.click_left_head_button_button()
        return element_exist

    def query_transferT_bank_list(self):
        '''
        用例编号：111CZSX035，所有功能-查询转账-快速转账
        测试点：银行列表，步骤：在快速转账里点击“银行名称”
        预期结果：进入银行列表
        :return:
        '''
        # 选择操作清单
        self.queryTransfer_handle.click_action_list_button('//*[contains(@text,"查询转账")]')
        self.queryTransfer_handle.click_payee_message_button()
        self.queryTransfer_handle.click_transfer_other_button()
        self.queryTransfer_handle.click_transfer_tomorrow_button()
        self.queryTransfer_handle.click_transfer_bank_name_button()

        # 取温馨提示属性，再返回
        element_exist = self.queryTransfer_page.get_bank_list_element().is_enabled()
        # self.driver.find_element_by_id('com.gdnybank.m:id/lv_bank_list')
        print('银行列表元素存在：', element_exist)
        if element_exist:
            for i in range(3):
                # 返回收款人信息页面
                # 返回转账页面
                # 返回到移动银行主页面
                self.queryTransfer_handle.click_left_head_button_button()
        return element_exist

    def query_transferT_bank_search(self):
        '''
        用例编号：111CZSX036，所有功能-查询转账-快速转账
        测试点：搜索银行名称，步骤：在银行列表搜索栏里输入银行名称，点击搜索
        预期结果：能搜索出该银行（支持模糊搜索）
        :return:
        '''
        # 选择操作清单
        self.queryTransfer_handle.click_action_list_button('//*[contains(@text,"查询转账")]')
        self.queryTransfer_handle.click_payee_message_button()
        self.queryTransfer_handle.click_transfer_other_button()
        self.queryTransfer_handle.click_transfer_bank_name_button()
        search_bank = self.read_excel.get_cell(41, 13)
        print('search_bank:', search_bank)
        self.queryTransfer_handle.send_search_bank_code(search_bank)
        self.queryTransfer_handle.click_search_button_button()

        # 取温馨提示属性，再返回
        search_bank_element = self.read_excel.get_cell(41, 14)
        print('search_bank_element:', search_bank_element)
        element_exist = self.queryTransfer_page.get_bank_list_element().find_element_by_xpath(search_bank_element)
        print('获取银行元素：', element_exist)
        if element_exist:
            for i in range(3):
                # 返回收款人信息页面
                # 返回转账页面
                # 返回到移动银行主页面
                self.queryTransfer_handle.click_left_head_button_button()
        return element_exist

    def query_transferT_payee_list(self):
        '''
        用例编号：111CZSX037，所有功能-查询转账-快速转账
        测试点：收款人名册，步骤：进入快速转账，点击账户姓名右侧的图标
        预期结果：进入收款人列表，列表内显示进行过交易的收款人信息
        :return:
        '''
        # 选择操作清单
        self.queryTransfer_handle.click_action_list_button('//*[contains(@text,"查询转账")]')
        self.queryTransfer_handle.click_payee_message_button()
        self.queryTransfer_handle.click_transfer_other_button()
        self.queryTransfer_handle.click_transfer_tomorrow_button()
        self.queryTransfer_handle.click_transfer_payee_head_button()

        # 取温馨提示属性，再返回
        # 取的是收款人列表的银行卡号元素
        element_exist = self.queryTransfer_page.get_bank_list_card_element()
        print('获取收款人列表元素：', element_exist)
        if element_exist:
            if element_exist:
                for i in range(3):
                    # 返回收款人信息页面
                    # 返回转账页面
                    # 返回到移动银行主页面
                    self.queryTransfer_handle.click_left_head_button_button()
        return element_exist

    def query_transferT_payee_choice(self):
        '''
        用例编号：111CZSX038，所有功能-查询转账-快速转账
        测试点：选择收款人，步骤：在收款人列表，点击其中一个收款人信息
        预期结果：自动返回上一页面，且账户姓名、收款人账号、银行名称已自动填写为选择的收款人信息
        :return:
        '''
        # 选择操作清单
        self.queryTransfer_handle.click_action_list_button('//*[contains(@text,"查询转账")]')
        self.queryTransfer_handle.click_payee_message_button()
        self.queryTransfer_handle.click_transfer_other_button()
        self.queryTransfer_handle.click_transfer_tomorrow_button()
        self.queryTransfer_handle.click_transfer_payee_head_button()

        # 选择收款人页面列表，具体的收款人在excel维护
        payee_name = self.read_excel.get_cell(65, 8)
        print('payee_name:', payee_name)
        self.queryTransfer_handle.click_bank_list_list(payee_name)
        # driver.find_elements_by_class_name("android.wdget.RelativeLayout").__getitem__(1).click()

        # 返回到收款人信息页面，取的是收款人账号元素
        element_code = self.queryTransfer_page.get_payee_account_element().get_attribute("text")
        # self.driver.find_element_by_id('com.gdnybank.m:id/tv_card_num')
        print('获取到的元素：', element_code)
        element_length = len(element_code)
        print('元素长度：', element_length)
        element_compare = (element_length > 8)  # 考虑到还没输入账号时，是5位字符，账号可能至少有8位
        if element_compare:
            for i in range(2):
                # 返回转账页面
                # 返回到移动银行主页面
                self.queryTransfer_handle.click_left_head_button_button()
        return element_compare

    def query_transferT_payee_add(self):
        '''
        用例编号：111CZSX039，所有功能-查询转账-快速转账
        测试点：添加收款人，步骤：进行一笔快速转账交易
        预期结果：交易成功后自动将该收款人添加进收款人名册
        :return: payeelist_compare
        '''

        # 选择操作清单
        self.queryTransfer_handle.click_action_list_button('//*[contains(@text,"查询转账")]')
        self.queryTransfer_handle.click_payee_message_button()
        self.queryTransfer_handle.click_transfer_other_button()
        self.queryTransfer_handle.click_transfer_tomorrow_button()
        self.queryTransfer_handle.click_transfer_payee_head_button()

        # 添加收款人前的收款人清单数量
        # payeelist_before = self.queryTransfer_page.get_bank_list_card_element()
        # print('添加前元素：' ,payeelist_before)
        payeelist_length_before = len(self.queryTransfer_page.get_bank_list_card_element())
        print('添加前：', payeelist_length_before)

        # 返回转账页面
        self.queryTransfer_handle.click_left_head_button_button()
        payee_name = self.read_excel.get_cell(66, 8)
        print('payee_name:', payee_name)
        self.queryTransfer_handle.send_payee_name_code(payee_name)

        # 判断当所输入账号与预期的不一致时，则输入，否则继续下一步选择银行名称
        payee_account = self.read_excel.get_cell(66, 9)
        print('payee_account:', payee_account)
        payee_account_after = 1
        while payee_account != payee_account_after:
            # payee_account = '6235 9574 0000 6141 031'
            # 清除
            self.queryTransfer_handle.clear_payee_account_code()
            time.sleep(5)
            # 输入银行账号
            input_element = self.queryTransfer_page.get_payee_account_element()
            input_element.click()
            self.press_Keycode.press_Keycode(payee_account, input_element)

            # self.queryTransfer_handle.send_payee_account_code(payee_account)
            # 获取输入后的银行账号
            time.sleep(2)

            payee_account_after_original = self.queryTransfer_page.get_payee_input_element()[1].get_attribute("text")
            # print('payee_account_after_original:', payee_account_after_original)
            payee_account_after = "".join(payee_account_after_original.split())  # 将输入后的银行卡号空格去掉再对比结果
            print('输入后银行账号：', payee_account_after)

        self.queryTransfer_handle.click_transfer_bank_name_button()
        time.sleep(2)
        payee_bank = self.read_excel.get_cell(66, 10)
        print('payee_bank:', payee_bank)
        self.queryTransfer_handle.click_bank_list_list(payee_bank)
        time.sleep(2)
        self.queryTransfer_handle.click_submit_transfer_button()
        time.sleep(2)
        # 调用转账页面方法
        self.query_transfer_page(66, 11, 66, 7, 66, 12) # 更新转账数据

        # 选择操作清单
        self.queryTransfer_handle.click_action_list_button('//*[contains(@text,"查询转账")]')
        self.queryTransfer_handle.click_payee_message_button()
        self.queryTransfer_handle.click_transfer_other_button()
        self.queryTransfer_handle.click_transfer_tomorrow_button()
        self.queryTransfer_handle.click_transfer_payee_head_button()

        # 添加新的收款人后的收款人清单数量
        # payeelist_after = self.queryTransfer_page.get_bank_list_card_element()
        payeelist_length_after = len(self.queryTransfer_page.get_bank_list_card_element())
        print('添加后：', payeelist_length_after)
        payeelist_compare = (payeelist_length_before < payeelist_length_after)
        print('对比结果：', payeelist_compare)
        if payeelist_compare:
            for i in range(3):
                # 返回收款人信息页面
                # 返回转账页面
                # 返回到移动银行主页面
                self.queryTransfer_handle.click_left_head_button_button()

        keyword = '确认'
        confirm = '确认'
        while keyword in confirm:
            confirm_element = self.queryTransfer_page.get_error_confirm_element()
            # print('confirm_element:', confirm_element)
            confirm = confirm_element[0].get_attribute('text')
            # print('弹框信息关键词：', confirm)
            confirm_element[0].click()

        return payeelist_compare

    def query_transferT_payee_delete_before(self):
        '''
        用例编号：111CZSX040，所有功能-查询转账-快速转账
        测试点：删除收款人，步骤：在收款人列表，点击右上角编辑，然后点击某收款人左侧删除按钮
        预期结果：成功删除该收款人信息
        本方法是记录删除前得到需要删除的选项，返回i
        :return: i
        '''
        # 选择操作清单
        self.queryTransfer_handle.click_action_list_button('//*[contains(@text,"查询转账")]')
        self.queryTransfer_handle.click_payee_message_button()
        self.queryTransfer_handle.click_transfer_other_button()
        self.queryTransfer_handle.click_transfer_tomorrow_button()
        self.queryTransfer_handle.click_transfer_payee_head_button()

        self.queryTransfer_handle.click_payee_list_edit_button()
        # 获取要删除的收款人元素-》再获取按照银行名称查询的id定位元素-》for再while语句判断删除收款人元素排在第几位，得到i+1
        # 最后使用删除按钮find_elements_by_id('删除id')[i+1].click()
        payee_name_target = self.read_excel.get_cell(67, 15)
        print('payee_name_target:', payee_name_target)

        # targets_element = self.driver.find_elements_by_id('com.gdnybank.m:id/tv_name_payee_contant_item')
        targets_element = self.queryTransfer_page.get_payee_list_name_element()
        # print('收款人列表元素：' ,targets_element)
        targets_element_length = len(targets_element)
        print('收款人列表元素长度：', targets_element_length)
        for i in range(targets_element_length):
            payee_name = targets_element[i].get_attribute('text')
            print('第' + str(i) + '收款人名字：', payee_name)
            if payee_name_target == payee_name:
                print('收款人元素数组：', i)
                return i

    def query_transferT_payee_delete(self):
        '''
        用例编号：111CZSX040，所有功能-查询转账-快速转账
        测试点：删除收款人，步骤：在收款人列表，点击右上角编辑，然后点击某收款人左侧删除按钮
        预期结果：成功删除该收款人信息
        :return: payeelist_compare_length
        '''
        # 调用删除前需要删除的元素第几位元素
        j = self.query_transferG_payee_delete_before()
        print('取到值：', j)
        # 删除收款人前的收款人清单数量
        payeelist_length_before = len(self.queryTransfer_page.get_bank_list_card_element())
        print('删除前长度：', payeelist_length_before)
        # delete_element = self.driver.find_elements_by_id('com.gdnybank.m:id/btn_del_payee_contact_item')[j]
        delete_element = self.queryTransfer_page.get_payee_delete_element()[j]
        delete_element.click()
        # self.queryTransfer_handle.click_payee_delete_button()
        payeelist_length_after = len(self.queryTransfer_page.get_bank_list_card_element())
        print('删除后长度：', payeelist_length_after)
        payeelist_compare = (payeelist_length_before > payeelist_length_after)
        print('对比结果：', payeelist_compare)
        if payeelist_compare:
            self.queryTransfer_handle.click_payee_list_complete_button()
            for i in range(3):
                # 返回收款人信息页面
                # 返回转账页面
                # 返回到移动银行主页面
                self.queryTransfer_handle.click_left_head_button_button()
        return payeelist_compare

    def query_transferT_payee_cityChoice(self):
        '''
        用例编号：111CZSX041，所有功能-查询转账-快速转账
        测试点：收款支行选择，步骤：点击银行名称进入银行列表，点击某其他银行
        预期结果：进入支行选择页面
        :return:
        '''
        # 选择操作清单
        self.queryTransfer_handle.click_action_list_button('//*[contains(@text,"查询转账")]')
        self.queryTransfer_handle.click_payee_message_button()
        self.queryTransfer_handle.click_transfer_tomorrow_button()
        self.queryTransfer_handle.click_transfer_other_button()
        # self.queryTransfer_handle.click_transfer_payee_head_button()

        self.queryTransfer_handle.click_transfer_bank_name_button()
        payee_bank = self.read_excel.get_cell(68, 13)
        print('payee_bank:', payee_bank)
        self.queryTransfer_handle.click_bank_list_list(payee_bank)
        # 进入南粤银行以外的银行，显示支行信息
        # 获取支行页面的关键字来验证
        self.queryTransfer_handle.click_search_city_button()
        # 如果选择非广州的城市，则需要先查询，但如果是热门城市，搜索再选择，会有两个搜索结果
        # self.queryTransfer_handle.send_search_city_code('广州')
        # self.queryTransfer_handle.click_city_branch_search_button()
        # 可能是find_elements
        city = self.read_excel.get_cell(68, 16)
        print('city:', city)
        # citys_element = self.driver.find_elements_by_id('com.gdnybank.m:id/city')
        citys_element = self.queryTransfer_page.get_city_list_element()
        # print('城市列表元素：' ,citys_element)
        citys_element_length = len(citys_element)
        print('城市列表元素长度：', citys_element_length)
        for i in range(citys_element_length):
            city_name = citys_element[i].get_attribute('text')
            print('第' + str(i) + '城市：', city_name)
            if city == city_name:
                # print('城市元素数组：', i)
                return i

    def query_transferT_payee_branch(self):
        '''
        用例编号：111CZSX041，所有功能-查询转账-快速转账
        测试点：收款支行选择，步骤：点击银行名称进入银行列表，点击某其他银行
        预期结果：进入支行选择页面
        :return:
        '''
        # 调用查看前需要搜索城市在第几位元素
        j = self.query_transferG_payee_cityChoice()
        # print('城市元素取到值：',j)
        city_elements = self.queryTransfer_page.get_city_list_element()[j]
        city_elements.click()
        self.queryTransfer_handle.click_branch_search_button()
        branch_amount = self.queryTransfer_page.get_branch_bank_amount_element().get_attribute('text')
        print('获取的属性：', branch_amount)
        branch_amountRe = re.sub("\D", "", branch_amount)
        print('抽取出来的数字有：', branch_amountRe)
        compare_branch_amount = branch_amountRe > '0'
        if compare_branch_amount:
            for i in range(4):
                self.queryTransfer_handle.click_left_head_button_button()
        return compare_branch_amount

    def query_transferT_payee_city(self):
        '''
        用例编号：111CZSX042，所有功能-查询转账-快速转账
        测试点：选择转入账号城市，步骤：点击城市名称搜索栏
        预期结果：弹出城市列表
        :return:
        '''
        # 选择操作清单
        self.queryTransfer_handle.click_action_list_button('//*[contains(@text,"查询转账")]')
        self.queryTransfer_handle.click_payee_message_button()
        self.queryTransfer_handle.click_transfer_other_button()
        self.queryTransfer_handle.click_transfer_tomorrow_button()
        # self.queryTransfer_handle.click_transfer_payee_head_button()

        self.queryTransfer_handle.click_transfer_bank_name_button()
        payee_bank = self.read_excel.get_cell(69, 13)
        print('payee_bank:', payee_bank)
        self.queryTransfer_handle.click_bank_list_list(payee_bank)
        # 进入南粤银行以外的银行，显示支行信息
        # 获取支行页面的关键字来验证

        self.queryTransfer_handle.click_search_city_button()
        verify_title = '城市列表'
        city_list = self.queryTransfer_page.get_title_head_element().get_attribute('text')
        print('获取到的头条标题：', city_list)
        city_compare = (city_list == verify_title)
        print('城市列表对比结果：', city_compare)
        if city_list == verify_title:
            for i in range(5):
                self.queryTransfer_handle.click_left_head_button_button()
        return city_list

    def query_transferT_branch_keyword(self):
        '''
        用例编号：111CZSX043，所有功能-查询转账-快速转账
        测试点：支行关键字搜索，步骤：选择城市后，输入关键字进行搜索
        预期结果：成功搜索出该城市下有该关键字的支行
        :return:
        '''
        # 调用查看前需要搜索城市在第几位元素
        j = self.query_transferT_payee_cityChoice()
        print('城市元素取到值：', j)
        city_elements = self.queryTransfer_page.get_city_list_element()[j]
        city_elements.click()
        self.queryTransfer_handle.click_branch_search_button()
        time.sleep(5)
        branch_amount = self.queryTransfer_page.get_branch_bank_amount_element().get_attribute('text')
        print('获取的属性：', branch_amount)
        branch_amountRe = re.sub("\D", "", branch_amount)
        print('抽取出来的数字有：', branch_amountRe)
        compare_branch_amount = branch_amountRe > '0'
        if compare_branch_amount:
            print('查询分行信息正常')
        branchKeyword = self.read_excel.get_cell(70, 17)
        self.queryTransfer_handle.send_branch_keyword_code(branchKeyword)
        self.queryTransfer_handle.click_branch_search_button()
        branch_bank = self.queryTransfer_page.get_branch_bank_keyword_element()
        print('分行查询结果元素：', branch_bank)
        if branch_bank != None:
            for i in range(4):
                self.queryTransfer_handle.click_left_head_button_button()
        return branch_bank

    def query_transferT_account_detail(self):
        '''
        用例编号：111CZSX044，所有功能-查询转账-快速转账
        测试点：查看账户详情，步骤：点击卡片右下角的感叹号
        预期结果：进入对应账户的详情页面
        :return:
        '''
        # 选择操作清单
        self.queryTransfer_handle.click_action_list_button('//*[contains(@text,"查询转账")]')
        time.sleep(2)
        self.queryTransfer_handle.click_account_plaint_button()
        # 获取账户详情的元素
        # 再打印账户详情的信息点到excel
        account_amount = len(self.queryTransfer_page.get_account_types_element())
        print('账户种类：', account_amount)
        account_message = []
        if account_amount > 0:
            for i in range(account_amount):
                account_types = self.queryTransfer_page.get_account_types_element()
                account_balances = self.queryTransfer_page.get_account_balance_element()
                regist_dates = self.queryTransfer_page.get_regist_date_element()
                acc_type = "acc_type" + str(i)
                account_balance = "account_balance" + str(i)
                regist_date = "regist_date" + str(i)
                print('赋值：', acc_type, ",", account_balance, ",", regist_date)
                acc_type = account_types[i].get_attribute('text')
                account_balance = account_balances[i].get_attribute('text')
                regist_date = regist_dates[i].get_attribute('text')
                account_message.append(acc_type)
                account_message.append(account_balance)
                account_message.append(regist_date)
                print('第' + str(i) + '账户种类：', acc_type)
                print('第' + str(i) + '账户余额：', account_balance)
                print('第' + str(i) + '开户日期：', regist_date)
                print('列表：', account_message)
                # self.write_excel.write(27, 18, account_message)
            print('列表account_message：', account_message)
            account_message_str = ",".join(account_message)
            print('列表转换为字符串：', account_message_str)
            self.write_excel.write(71, 18, account_message_str)

            for j in range(2):
                self.queryTransfer_handle.click_left_head_button_button()
        else:
            return None
        return account_amount



