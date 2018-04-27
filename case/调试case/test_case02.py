#coding=utf-8
'''
unittes使用
'''
import  sys
sys.path.append("E:\\AppiumProjectAndroid")
import unittest
import HTMLTestReportCN
import multiprocessing
import time
from util.server import Server
from business.login_business import LoginBusiness
from util.write_user_command import WriteUserCommand
# from appium import webdriver
# import os,re

class ParameTestCase(unittest.TestCase):
    def __init__(self,methodName='runTest',parame = None):
        '''
        构造参数
        :param methodName:
        :param parame:
        :return:
        '''
        super(ParameTestCase,self).__init__(methodName)
        global parames  #声明全局变量
        parames = parame

class CaseTest(ParameTestCase):

    #加上注解，在python叫容器，当有2个case的时候，是全局的，就运行一次
    #当前实例本身的一个函数
    @classmethod
    def setUpClass(cls):

        print('setUpclass--->',parames)
        cls.login_business = LoginBusiness(parames)

    def setUp(self):
        print('this is setup\n')
    # @unittest.skip('CaseTest')
    # 运行test_01前要运行setUP()
    def test_01(self):
        # self.assertEqual(3,3)
        print('test case 里面的参数',parames)
        self.login_business.login_pass()


    def test_02(self):
        self.assertEqual(2, 1, 'error')
        print('this is case02\n')


    # def test_03(self):
    #     self.assertEqual(2, 1, 'error')

    def tearDown(self):
        print('this is teardown！')

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
    # suite.addTest(CaseTest('test_02', parame = i))
    suite.addTest(CaseTest('test_01', parame = i))
    # unittest.TextTestRunner().run(suite)  #这一行和85行一起打开，会导致死循环
    html_file = "E:\\AppiumProjectAndroid\\report\\report"+str(i)+".html"
    fp = open(html_file,'wb')
    runner = HTMLTestReportCN.HTMLTestRunner(
        stream=fp,
        title='自动化测试报告',
        tester='Susun.Zeng'
        )
    runner.run(suite)
    # HTMLTestReportCN.HTMLTestRunner(stream=fp).run(suite)
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
    print('在什么情况？')
    for i in range(get_count()):       # for i in range(get_count())
        print("i:",i)
        # t = threading.Thread(target=get_suite, args=(i,))  # 注意args=(i,)要加上逗号
        t = multiprocessing.Process(target=get_suite, args=(i,))
        threads.append(t)
        print('threads:', threads)
        # t.start()
    for j in threads:
        j.start()
        time.sleep(2)

    # #确定生成报告的路径
    # filePath ='E:\\AppiumProjectAndroid\\report\\report.html'
    # fp = open(filePath,'wb')
    # #生成报告的Title,描述
    # runner = HTMLTestReportCN.HTMLTestRunner(
    #     stream=fp,
    #     title='自动化测试报告',
    #     #description='详细测试用例结果',
    #     tester='Susun.Zeng'
    #     )
    # #运行测试用例
    # runner.run(get_suite())
    # # 关闭文件，否则会无法生成文件
    # fp.close()






