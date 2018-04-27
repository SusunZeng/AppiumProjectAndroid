# 调试添加按照i在for循环里做的test案例执行
# coding=utf-8
import sys
sys.path.append("E:\\AppiumProjectAndroid")
import unittest
import HTMLTestReportCN
import threading
import multiprocessing
from util.server import Server
import time
# from appium import webdriver
# # from business.login_business import LoginBusiness
# from util.write_user_command import WriteUserCommand
from util.opera_excel import OperaExcel
from util.write_excel import Write_Excel
from util.read_excel import Read_Excel

class ParameTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', parame=None):
        super(ParameTestCase, self).__init__(methodName)
        global parames
        parames = parame
        global opera_excel
        # opera_excel = OperaExcel(file_path='E:\\AppiumProjectAndroid\\config\\AndroidAutomationTestCase-1.xlsx')
        global write_excel
        global read_excel
        write_excel = Write_Excel('E:\\AppiumProjectAndroid\\config\\AndroidAutomationTestCase-1.xlsx')
        read_excel = Read_Excel('E:\\AppiumProjectAndroid\\config\\AndroidAutomationTestCase-1.xlsx','Sheet1')

class Case_Test(ParameTestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpclass---->", parames)
        # cls.login_business = LoginBusiness(parames)

    def setUp(self):
        print("this is setup\n")

    def test_1(self):
        print("test case 里面的参数", parames)
        print("this is case01\n")
        print('验证值01：',self.assertEqual('1', '1', '验证失败'))
        print('write/read excel方法test_1:',write_excel,',',read_excel)
        write_excel.write(2, 10, ' 03')
        time.sleep(2)
        print('test_1:',read_excel.get_cell(2 ,10))


    # @unittest.skip("CaseTest")
    def test_2(self):
        # self.login_business.login_user_error()
        print("this is case02\n")
        print('write/read excel方法test_1:', write_excel, ',', read_excel)
        verification_result = self.assertEqual('1', '1', '验证失败')
        print('verification_result:',verification_result)
        if verification_result == None:
            write_excel.write(3, 10, '通过')
            time.sleep(2)
            print('写入的值:',read_excel.get_cell(3, 10))
        else:
            # write_excel.write(3, 10, '失败')
            print('写入的值:', read_excel.get_cell(3, 10))
        # self.assertEqual('dkkdkkddfd', '取款密码输入不正确', '验证失败')
        # self.assertTrue(True)

    def test_3(self):
        print("test case 里面的参数", parames)
        print("this is case03\n")
        print('write/read excel方法test_1:', write_excel, ',', read_excel)
        code = '取款密码输入不正确'
        verification_result = self.assertEqual(code, '取款密码输入不正确', '验证失败')
        print('验证值02：', verification_result)
        write_excel.write(4, 10, '通过345+%$5')
        time.sleep(2)
        print('写入的值:', read_excel.get_cell(4, 10))
        # opera_excel.write_value(26, 10, 'failed')

    def tearDown(self):
        time.sleep(1)
        print('test_1:', read_excel.get_cell(2, 10))
        print('test_2:', read_excel.get_cell(3, 10))
        print('test_3:', read_excel.get_cell(4, 10))
        print("this is teardown\n")
        # if sys.exc_info()[0]:
        #     self.login_business.login_handle.login_page.driver.save_screenshot("../jpg/test02.png")
    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        print("this is class teardown\n")
    # cls.driver.quit()


def appium_init():
    server = Server()
    server.main()


def get_suite(i):
    print("get_suite里面的", i)
    suite = unittest.TestSuite()
    read_excel = Read_Excel('E:\\AppiumProjectAndroid\\config\\AndroidAutomationTestCase-1.xlsx', 'Sheet1')
    # suite.addTest(Case_Test("test_01", parame=i))
    # suite.addTest(Case_Test("test_03", parame=i))
    # print('read_excel:', read_excel)
    # rows = read_excel.get_rows()
    # print('rows方法get_suite:', rows)
    for j in range(1, 4):
        # print('j循环：', j)
        list = read_excel.get_excel_value("test_" + str(j))
        print("list:", list)
        if list[1] == "Y" and list[9] == None:
            print("符合条件的：", list[0])
            suite.addTest(Case_Test(list[0], parame=i))
        else:
            continue
            # print("不符合条件：", list[0])

    # #unittest.TextTestRunner().run(suite)  # 这行脚本不能与下方的runner.run(suite)同时调试执行
    html_file = "E:\\AppiumProjectAndroid\\report\\report" + str(i) + ".html"
    fp = open(html_file, "wb")
    HTMLTestReportCN.HTMLTestRunner(stream=fp).run(suite)
    fp.close()

    # fp = open(html_file, 'wb')
    # runner = HTMLTestReportCN.HTMLTestRunner(
    #     stream=fp,
    #     title='自动化测试报告',
    #     tester='Susun.Zeng'
    # )
    # runner.run(suite)
    # fp.close()

# def get_count():
#     write_user_file = WriteUserCommand()
#     count = write_user_file.get_file_lines()
#     return count


if __name__ == '__main__':
    # appium_init()
    # get_suite(0)
    threads = []
    for i in range(1):
        print(i)
        t = multiprocessing.Process(target=get_suite, args=(i,))
        threads.append(t)
    for j in threads:
        j.start()

    # time.sleep(1)
# time.sleep(80)