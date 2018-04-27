#coding=utf-8

# from publicMethod import loginApp
# import sys
# import importlib
# importlib.reload(sys)
# # reload(sys)   python 2.X版本
# # sys.setdefaultencoding('utf-8')
# sys.path.append("E:\AppiumProjectAndroid\public")
#
# # 单独调用startApp()
# # startApp.startApp().startApp()
# # publicFunction.publicFunction().startApp()
# loginApp.loginApp().loginApp()

# from util.pop_up_box import *

# pop_up_box = pop_up_box()
# print(pop_up_box)

# for i in range(1, 6):
#     if a = ''
#     print('案例名分别为：' + 'test_' + str(i))

# abc = get_lines
# allow =
# passname =
# for i in row(1, abc):
#     if allow == 'y' and passname == ''
#         if True:
#             print('案例名分别为：' + 'test_' + str(i))


# coding=utf-8
import sys
sys.path.append("E:\\AppiumProjectAndroid")
import unittest
import HTMLTestReportCN
import threading
import multiprocessing
from util.server import Server
import time
from appium import webdriver
# from business.login_business import LoginBusiness
from util.write_user_command import WriteUserCommand
from opera_excel_20180413 import OperaExcl


# class Opera_excel():
#     def __init__(self):
#         self.opera_excel = OperaExcl




class ParameTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', parame=None):
        super(ParameTestCase, self).__init__(methodName)
        global parames
        parames = parame


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
        print('验证值：',self.assertEqual('1', '1', '验证失败'))
        code = '取款密码输入不正确'
        print('验证值：', self.assertEqual(code, '取款密码输入不正确', '验证失败'))
        self.assertEqual('dkkdkkd', '取款密码输入不正确', '验证失败')

        # self.login_business.login_pass()

    # self.assertNotEqual(1,2)
    # self.assertTrue(flag)
    # self.assertFalse(flag)
    # @unittest.skip("CaseTest")
    def test_2(self):
        # self.login_business.login_user_error()
        print("this is case02\n")
        self.assertEqual('1', '0', '验证失败')
        self.assertEqual('dkkdkkddfd', '取款密码输入不正确', '验证失败')
        self.assertTrue(True)

    def test_3(self):
        print("this is test_3")
    def test_4(self):
        print("this is test_4090")
    def test_5(self):
        print("this is test_5")
    def test_6(self):
        print("this is test_6")


    def tearDown(self):
        time.sleep(1)
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
    opera = OperaExcl()
    #row = opera.get_lines()
    for ii in range(3,6):
        # list = OperaExcl().gets_excel_value("test_"+str(ii))
        list = opera.gets_excel_value("test_" + str(ii))
        # print("list:", list)
        if list[1] == "Y" and list[9] == "":
            print("符合条件的：", list[0])
            suite.addTest(Case_Test(list[0], parame=i))
        else:
            print("不符合条件：", list[0])

    #  unittest.TextTestRunner().run(suite)
    html_file = "E:\\AppiumProjectAndroid\\report\\report" + str(i) + ".html"
    fp = open(html_file, "wb")
    HTMLTestReportCN.HTMLTestRunner(stream=fp).run(suite)


# def get_count():
#     write_user_file = WriteUserCommand()
#     count = write_user_file.get_file_lines()
#     return count


if __name__ == '__main__':


    # appium_init()
    get_suite(0)
    # threads = []
    # for i in range(2):
    #
    #     t = multiprocessing.Process(target=get_suite, args=(i,))
    #     threads.append(t)
    # for j in threads:
    #     j.start()
    #
    # time.sleep(1)
# time.sleep(80)






