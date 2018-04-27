#coding=utf-8
'''
unittes使用
'''
import  sys
sys.path.append("E:\\AppiumProjectAndroid")
import unittest
import HTMLTestReportCN
import threading
import multiprocessing
from util.server import Server
import time
from util.write_user_command import WriteUserCommand
# from appium import webdriver
from business.login_business import Login_Business
from business.quitLogin_business import QuitLogin_Business
from business.queryTransfer_business import QueryTransfer_Business
from business.myAccount_business import MyAccount_Business
from base.base_driver import BaseDriver
from util.date_number import DataNumber3
from util.write_excel import Write_Excel
from util.read_excel import Read_Excel


class ParameTest_Case(unittest.TestCase):
    def __init__(self,methodName='runTest',parame = None):
        '''
        构造参数
        :param methodName:
        :param parame:
        :return:
        '''
        super(ParameTest_Case,self).__init__(methodName)
        global parames  #声明全局变量
        parames = parame
        global write_excel
        global read_excel
        write_excel = Write_Excel('E:\\AppiumProjectAndroid\\config\\AndroidAutomationTestCase.xlsx')
        read_excel = Read_Excel('E:\\AppiumProjectAndroid\\config\\AndroidAutomationTestCase.xlsx','Sheet1')

class CaseTest(ParameTest_Case):

    #加上注解，在python叫容器，当有2个case的时候，是全局的，就运行一次
    #当前实例本身的一个函数
    driver = None
    @classmethod
    def setUpClass(cls):
        global driver
        print('setUpClass--->',parames)
        # cls.login_business = LoginBusiness(parames)
        # # cls.quitLogin_business = QuitLoginBusiness(parames)
        # cls.driver = cls.login_business.drivers()
        # # return driver
        base_driver = BaseDriver()
        driver = base_driver.android_driver(parames)
        cls.login_business = Login_Business(driver)
        cls.queryTransfer_business = QueryTransfer_Business(driver)
        cls.quitLogin_business = QuitLogin_Business(driver)
        cls.myAccount_business = MyAccount_Business(driver)
        cls.login_business.login_before()

    def setUp(self):
        print('this is setup\n')
        # print('write_excel方法setUp:', write_excel)


    # 运行test_01前要运行setUP()
    # @unittest.skip('暂停CaseTest')
    def test_1(self):
        # self.assertEqual(3,3)
        print('test case_01 里面的参数',parames)
        # self.login_business.login_before()
        # self.login_business.login_user_error()
        user_flag = self.login_business.login_user_error()
        print('user_flag = ', user_flag)
        if user_flag == True:
            write_excel.write(2, 10, '通过')
        else:
            write_excel.write(2, 10, '失败')

    # @unittest.skip('暂停CaseTest')
    def test_2(self):
        # self.assertEqual(2, 1, 'error')
        print('this is case02\n')
        print('test case_02 里面的参数', parames)
        # self.login_business.login_before()
        self.login_business.login_pass()

    # @unittest.skip('暂停CaseTest')
    def test_3(self):
        self.queryTransfer_business.query_transferF_input()
        transfer_submitted_mark = self.queryTransfer_business.query_transfer_page(4, 11, 4, 7)
        verification_result = self.assertEqual(transfer_submitted_mark, '转账已提交', '验证失败')
        print('verification_result:',verification_result)
        if verification_result == None:
            write_excel.write(4, 10, '通过')
            # print('get_cell(4, 10):', read_excel.get_cell(4, 10))

    # @unittest.skip('暂停CaseTest')
    def test_4(self):
        # print('方法test_4：',driver)
        self.queryTransfer_business.query_transferF_select()
        transfer_submitted_mark = self.queryTransfer_business.query_transfer_page(5, 11, 5, 7)
        verification_result = self.assertEqual(transfer_submitted_mark, '转账已提交', '验证失败')
        print('verification_result:',verification_result)
        if verification_result == None:
            write_excel.write(5, 10, '通过')


    # @unittest.skip('暂停CaseTest')
    def test_5(self):
        error_prompt = self.queryTransfer_business.query_transferF_payee_space()
        print('温馨提示：', error_prompt)
        verification_result = self.assertEqual(error_prompt, '请输入账户姓名', '验证失败')
        print('verification_result:',verification_result)
        if verification_result == None:
            write_excel.write(6, 10, '通过')


    # @unittest.skip('暂停CaseTest')
    def test_6(self):
        # print('用例编号：111CZSX024')
        error_prompt = self.queryTransfer_business.query_transferF_amount_zero()
        print('温馨提示：', error_prompt)
        verification_result = self.assertEqual(error_prompt, '转账金额输入有误', '验证失败')
        print('verification_result:',verification_result)
        if verification_result == None:
            write_excel.write(7, 10, '通过')


    # @unittest.skip('暂停CaseTest')
    def test_7(self):
        error_prompt = self.queryTransfer_business.query_transferF_beyond_balance()
        print('温馨提示：', error_prompt)
        if error_prompt == 'MBS030212':
            # 设置单笔转账金额，交易金额不能大于单笔限额
            verification_result = self.assertEqual(error_prompt, 'MBS030212', '验证失败')
        else:
            verification_result = self.assertEqual(error_prompt, '余额不足', '验证失败')
        print('verification_result:', verification_result)
        if verification_result == None:
            write_excel.write(8, 10, '通过')


    # @unittest.skip('暂停CaseTest')
    def test_8(self):
        error_prompt = self.queryTransfer_business.query_transferF_amount_space()
        print('温馨提示：', error_prompt)
        verification_result = self.assertEqual(error_prompt, '请输入转账金额', '验证失败')
        print('verification_result:',verification_result)
        if verification_result == None:
            write_excel.write(9, 10, '通过')


    # @unittest.skip('暂停CaseTest')
    def test_9(self):
        error_prompt = self.queryTransfer_business.query_transferF_amount_capital()
        print('温馨提示：', error_prompt)
        verification_result = self.assertEqual(error_prompt, '请输入转账金额', '验证失败')
        print('verification_result:',verification_result)
        if verification_result == None:
            write_excel.write(10, 10, '通过')


    # @unittest.skip('暂停CaseTest')
    def test_10(self):
        error_prompt = self.queryTransfer_business.query_transferF_payee_wrong()
        print('温馨提示：', error_prompt)
        verification_result = self.assertEqual(error_prompt, '账户和户名不匹配', '验证失败')
        print('verification_result:',verification_result)
        if verification_result == None:
            write_excel.write(11, 10, '通过')


    # @unittest.skip('暂停CaseTest')
    def test_11(self):
        transfer_submitted_mark = self.queryTransfer_business.query_transferF_same_payer()
        print('转账成功提示：', transfer_submitted_mark)
        verification_result = self.assertEqual(transfer_submitted_mark, '转入转出账户不能相同', '验证失败')
        print('verification_result:',verification_result)
        if verification_result == None:
            write_excel.write(12, 10, '通过')


    # @unittest.skip('暂停CaseTest')
    def test_12(self):
        error_prompt = self.queryTransfer_business.query_transferF_drawpassword_wrong()
        print('温馨提示：', error_prompt)
        verification_result = self.assertEqual(error_prompt, '您已输错密码[1]次,再输错[2]次,将锁卡', '验证失败')
        print('verification_result:',verification_result)
        if verification_result == None:
            write_excel.write(13, 10, '通过')


    # @unittest.skip('暂停CaseTest')
    def test_13(self):
        transfer_submitted_mark = self.queryTransfer_business.query_transferF_drawpassword_again()
        print('转账成功提示：', transfer_submitted_mark)
        verification_result = self.assertEqual(transfer_submitted_mark, '转账已提交', '验证失败')
        print('verification_result:',verification_result)
        if verification_result == None:
            write_excel.write(14, 10, '通过')


    # @unittest.skip('暂停CaseTest')    #由于涉及到锁卡，暂时不执行
    def test_14(self):
        error_prompt = self.queryTransfer_business.query_transferF_drawpassword_lock()
        print('温馨提示：', error_prompt)
        verification_result = self.assertEqual(error_prompt, '您已输错密码[1]次,再输错[2]次,将锁卡', '验证失败')
        print('verification_result:',verification_result)
        if verification_result == None:
            write_excel.write(15, 10, '通过')


    # @unittest.skip('暂停CaseTest')
    def test_15(self):
        error_prompt = self.queryTransfer_business.query_transferF_drawpassword_lack()
        print('温馨提示：', error_prompt)
        verification_result = self.assertEqual(error_prompt, '取款密码输入不正确，请重新输入', '验证失败')
        print('verification_result:',verification_result)
        if verification_result ==None:
            write_excel.write(16, 10, '通过')


    # @unittest.skip('暂停CaseTest')
    def test_16(self):
        element_exist = self.queryTransfer_business.query_transferF_drawpassword_excess()
        # print('获取的元素：', element_exist)
        verification_result = self.assertIsNotNone(element_exist, '输入取款密码超过6位失败')
        print('verification_result:',verification_result)
        if verification_result == None:
            write_excel.write(17, 10, '通过')


    # @unittest.skip('暂停CaseTest')
    def test_17(self):
        element_exist = self.queryTransfer_business.query_transferF_bank_list()
        print('获取的元素：', element_exist)
        verification_result = self.assertIsNotNone(element_exist, '进入银行列表失败')
        print('verification_result:',verification_result)
        if verification_result == None:
            write_excel.write(18, 10, '通过')


    # @unittest.skip('暂停CaseTest')
    def test_18(self):
        element_exist = self.queryTransfer_business.query_transferF_bank_search()
        # print('获取的元素：', element_exist)
        verification_result = self.assertIsNotNone(element_exist, '搜索银行名称失败')
        print('verification_result:',verification_result)
        if verification_result == None:
            write_excel.write(19, 10, '通过')


    # @unittest.skip('暂停CaseTest')
    def test_19(self):
        element_exist = self.queryTransfer_business.query_transferF_payee_list()
        # print('获取的元素：', element_exist)
        print(self.assertIsNotNone(element_exist, '进入收款人列表失败'))
        write_excel.write(20, 10, '通过')


    # @unittest.skip('暂停CaseTest')
    def test_20(self):
        element_compare = self.queryTransfer_business.query_transferF_payee_choice()
        print('获取元素长度对比结果：', element_compare)
        print(self.assertTrue(element_compare, '选择收款人信息失败'))
        write_excel.write(21, 10, '通过')


    # @unittest.skip('暂停CaseTest')
    def test_21(self):
        payeelist_compare = self.queryTransfer_business.query_transferF_payee_add()
        print('获取元素长度对比结果：', payeelist_compare)
        print(self.assertTrue(payeelist_compare, '添加收款人信息失败'))
        write_excel.write(22, 10, '通过')


    # @unittest.skip('暂停CaseTest')
    def test_22(self):
        payeelist_compare = self.queryTransfer_business.query_transferF_payee_delete()
        print('获取元素长度对比结果：', payeelist_compare)
        print(self.assertTrue(payeelist_compare, '删除收款人信息失败'))
        write_excel.write(23, 10, '通过')


    # @unittest.skip('暂停CaseTest')
    def test_23(self):
        compare_branch_amount = self.queryTransfer_business.query_transferF_payee_branch()
        print('获取支行数量对比结果：', compare_branch_amount)
        print(self.assertTrue(compare_branch_amount, '进入支行页面失败'))
        write_excel.write(24, 10, '通过')


    # @unittest.skip('暂停CaseTest')
    def test_24(self):
        city_list = self.queryTransfer_business.query_transferF_payee_city()
        print('获取城市列表页面标题：', city_list)
        print(self.assertIsNotNone(city_list, '弹出城市列表页面失败'))
        write_excel.write(25, 10, '通过')


    # @unittest.skip('暂停CaseTest')
    def test_25(self):
        branch_bank = self.queryTransfer_business.query_transferF_branch_keyword()
        print('获取分行查询结果：', branch_bank)
        print(self.assertIsNotNone(branch_bank, '关键字分行查询失败'))
        write_excel.write(26, 10, '通过')


    # @unittest.skip('暂停CaseTest')
    def test_26(self):
        account_amount = self.queryTransfer_business.query_transferF_account_detail()
        print('获取账户种类有：' ,account_amount)
        print(self.assertIsNotNone(account_amount, '获取账户种类失败'))
        write_excel.write(27, 10, '通过')


    # @unittest.skip('暂停CaseTest')
    def test_27(self):
        self.queryTransfer_business.query_transferG_select()
        transfer_submitted_mark = self.queryTransfer_business.query_transfer_page(28, 11, 28, 7)
        # self.myAccount_business.hide_balance()
        verification_result = self.assertEqual(transfer_submitted_mark, '转账已提交', '验证失败')
        print('verification_result:',verification_result)
        if verification_result == None:
            write_excel.write(28, 10, '通过')


    # @unittest.skip('暂停CaseTest')
    def test_28(self):
        error_prompt = self.queryTransfer_business.query_transferG_amount_zero()
        verification_result = self.assertEqual(error_prompt, '转账金额输入有误', '验证失败')
        print('verification_result:',verification_result)
        if verification_result == None:
            write_excel.write(29, 10, '通过')


    # @unittest.skip('暂停CaseTest')
    def test_29(self):
        error_prompt = self.queryTransfer_business.query_transferG_beyond_balance()
        verification_result = self.assertEqual(error_prompt, '余额不足', '验证失败')
        print('verification_result:',verification_result)
        if verification_result == None:
            write_excel.write(30, 10, '通过')


    # @unittest.skip('暂停CaseTest')
    def test_30(self):
        error_prompt = self.queryTransfer_business.query_transferG_amount_space()
        verification_result = self.assertEqual(error_prompt, '请输入转账金额', '验证失败')
        print('verification_result:',verification_result)
        if verification_result == None:
            write_excel.write(31, 10, '通过')



    # @unittest.skip('暂停CaseTest')
    def test_31(self):
        error_prompt = self.queryTransfer_business.query_transferG_amount_capital()
        verification_result = self.assertEqual(error_prompt, '请输入转账金额', '验证失败')
        print('verification_result:',verification_result)
        if verification_result == None:
            write_excel.write(32, 10, '通过')

    # @unittest.skip('暂停CaseTest')
    def test_32(self):
        error_prompt = self.queryTransfer_business.query_transferG_payee_wrong()
        verification_result = self.assertEqual(error_prompt, '账户和户名不匹配', '验证失败')
        print('verification_result:', verification_result)
        if verification_result == None:
            write_excel.write(33, 10, '通过')

    # @unittest.skip('暂停CaseTest')
    def test_33(self):
        error_prompt = self.queryTransfer_business.query_transferG_payee_space()
        verification_result = self.assertEqual(error_prompt, '请输入账户姓名', '验证失败')
        print('verification_result:', verification_result)
        if verification_result == None:
            write_excel.write(34, 10, '通过')

    # @unittest.skip('暂停CaseTest')
    def test_34(self):
        transfer_submitted_mark = self.queryTransfer_business.query_transferG_same_payer()
        verification_result = self.assertEqual(transfer_submitted_mark, '转入转出账户不能相同', '验证失败')
        print('verification_result:', verification_result)
        if verification_result == None:
            write_excel.write(35, 10, '通过')

    # @unittest.skip('暂停CaseTest')
    def test_35(self):
        error_prompt = self.queryTransfer_business.query_transferG_drawpassword_wrong()
        verification_result = self.assertEqual(error_prompt, '您已输错密码[1]次,再输错[2]次,将锁卡', '验证失败')
        print('verification_result:', verification_result)
        if verification_result == None:
            write_excel.write(36, 10, '通过')

    # @unittest.skip('暂停CaseTest')
    def test_36(self):
        transfer_submitted_mark = self.queryTransfer_business.query_transferG_drawpassword_again()
        verification_result = self.assertEqual(transfer_submitted_mark, '转账已提交', '验证失败')
        print('verification_result:', verification_result)
        if verification_result == None:
            write_excel.write(37, 10, '通过')

    # @unittest.skip('暂停CaseTest')
    def test_37(self):
        error_prompt = self.queryTransfer_business.query_transferG_drawpassword_lack()
        verification_result = self.assertEqual(error_prompt, '取款密码输入不正确，请重新输入', '验证失败')
        print('verification_result:', verification_result)
        if verification_result == None:
            write_excel.write(38, 10, '通过')

    # @unittest.skip('暂停CaseTest')
    def test_38(self):
        element_exist = self.queryTransfer_business.query_transferG_drawpassword_excess()
        verification_result = self.assertIsNotNone(element_exist, '输入取款密码超过6位失败')
        print('verification_result:', verification_result)
        if verification_result == None:
            write_excel.write(39, 10, '通过')

    # @unittest.skip('暂停CaseTest')
    def test_39(self):
        element_exist = self.queryTransfer_business.query_transferG_bank_list()
        verification_result = self.assertIsNotNone(element_exist, '进入银行列表失败')
        print('verification_result:', verification_result)
        if verification_result == None:
            write_excel.write(40, 10, '通过')

    # @unittest.skip('暂停CaseTest')
    def test_40(self):
        element_exist = self.queryTransfer_business.query_transferG_bank_search()
        verification_result = self.assertIsNotNone(element_exist, '搜索银行名称失败')
        print('verification_result:', verification_result)
        if verification_result == None:
            write_excel.write(41, 10, '通过')

    # @unittest.skip('暂停CaseTest')
    def test_41(self):
        element_exist = self.queryTransfer_business.query_transferG_payee_list()
        verification_result = self.assertIsNotNone(element_exist, '进入收款人列表失败')
        print('verification_result:', verification_result)
        if verification_result == None:
            write_excel.write(42, 10, '通过')

    # @unittest.skip('暂停CaseTest')
    def test_42(self):
        element_compare = self.queryTransfer_business.query_transferG_payee_choice()
        verification_result = self.assertTrue(element_compare, '选择收款人信息失败')
        print('verification_result:', verification_result)
        if verification_result == None:
            write_excel.write(43, 10, '通过')

    # @unittest.skip('暂停CaseTest')
    def test_43(self):
        payeelist_compare = self.queryTransfer_business.query_transferG_payee_add()
        verification_result = self.assertTrue(payeelist_compare, '添加收款人信息失败')
        print('verification_result:', verification_result)
        if verification_result == None:
            write_excel.write(44, 10, '通过')

    # @unittest.skip('暂停CaseTest')
    def test_44(self):
        payeelist_compare = self.queryTransfer_business.query_transferG_payee_delete()
        verification_result = self.assertTrue(payeelist_compare, '删除收款人信息失败')
        print('verification_result:',verification_result)
        if verification_result == None:
            write_excel.write(45, 10, '通过')

    # @unittest.skip('暂停CaseTest')
    def test_45(self):
        compare_branch_amount = self.queryTransfer_business.query_transferG_payee_branch()
        verification_result = self.assertTrue(compare_branch_amount, '进入支行页面失败')
        print('verification_result:', verification_result)
        if verification_result == None:
            write_excel.write(46, 10, '通过')

    # @unittest.skip('暂停CaseTest')
    def test_46(self):
        city_list = self.queryTransfer_business.query_transferG_payee_city()
        verification_result = self.assertIsNotNone(city_list, '弹出城市列表页面失败')
        print('verification_result:', verification_result)
        if verification_result == None:
            write_excel.write(47, 10, '通过')

    # @unittest.skip('暂停CaseTest')
    def test_47(self):
        branch_bank = self.queryTransfer_business.query_transferG_branch_keyword()
        verification_result = self.assertIsNotNone(branch_bank, '关键字分行查询失败')
        print('verification_result:', verification_result)
        if verification_result == None:
            write_excel.write(48, 10, '通过')

    # @unittest.skip('暂停CaseTest')
    def test_48(self):
        account_amount = self.queryTransfer_business.query_transferG_account_detail()
        verification_result = self.assertIsNotNone(account_amount, '获取账户种类失败')
        print('verification_result:', verification_result)
        if verification_result == None:
            write_excel.write(49, 10, '通过')

    @unittest.skip('暂停CaseTest')
    def test_49(self):
        pass

    @unittest.skip('暂停CaseTest')
    def test_100(self):
        self.quitLogin_business.quitLogin_pass()

    def tearDown(self):
        time.sleep(1)
        print('this is teardown！')
        #错误截图方法,sys.exc_info():是python自动捕抓异常的语句
        if sys.exc_info()[0]:
            self.login_business.login_handle.login_page.driver.save_screenshot('../jpg/test01.png')

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        print('this is class teardown.\n')

def appium_init():
    print('从这里开始启动appium')
    server = Server()
    server.main()

def get_suite(i):
    '''
    设计testcase执行顺序，以及生成报告
    :param i:
    :return:
    '''
    print('get_suite里面的', i)
    suite = unittest.TestSuite()
    read_excel = Read_Excel('E:\\AppiumProjectAndroid\\config\\AndroidAutomationTestCase.xlsx', 'Sheet1')
    print('read_excel方法get_suite:', read_excel)
    rows = read_excel.get_rows()
    print('rows方法get_suite:',rows)
    for j in range(1, 50):
        # print('j循环：', j)
        list = read_excel.get_excel_value("test_" + str(j))
        # print("list:", list)
        if list[1] == "Y" and list[9] == None:
            # print("符合条件的：", list[0])
            suite.addTest(CaseTest(list[0], parame=i))
        else:
            continue
            # print("不符合条件：", list[0])

    # for j in range(1,32):
    #
    #     suite.addTest(CaseTest('test_'+ str(j), parame=i))

    strnow_number3 = DataNumber3()
    html_file = "E:\\AppiumProjectAndroid\\report\\report" + strnow_number3 + str(i) + ".html"
    # print('文件名：', html_file)
    fp = open(html_file,'wb')
    runner = HTMLTestReportCN.HTMLTestRunner(
        stream=fp,
        title='自动化测试报告',
        tester='Susun.Zeng'
        )
    runner.run(suite)
    fp.close()

def get_count():
    '''
    返回设备个数
    :return:count
    '''
    write_user_file = WriteUserCommand()
    count = write_user_file.get_file_lines()
    print('count:',count)
    return count


if __name__ == '__main__':
    print('启动appium')
    appium_init()
    threads = []
    # print('在什么情况？')
    for i in range(get_count()):       # for i in range(get_count())
        print("i:",i)
        # t = threading.Thread(target=get_suite, args=(i,))  # 注意args=(i,)要加上逗号
        t = multiprocessing.Process(target=get_suite, args=(i,))
        threads.append(t)
        # print('threads:', threads)
        # t.start()
    for j in threads:
        j.start()
        time.sleep(2)







