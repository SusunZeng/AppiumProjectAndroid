#coding=utf-8
'''
unittes使用
'''
import unittest
import multiprocessing
import time
import HTMLTestReportCN

class CaseTest(unittest.TestCase):
    # @classmethod叫容器
    @classmethod
    def setUpClass(cls):
        print('this is class')

    def setUp(self):
        print('this is setup')
    def test_01(self):
        flag = True
        print('this is case')
        # 验证是否相等
        # self.assertEqual(1,2,'数据错误')
        self.assertNotEqual(1,2)
        self.assertTrue(flag)
        # self.assertFalse(flag)
    #传递函数，把类的名字传参数
    #添加下面这行，可以跳过test_02()执行
    # @unittest.skip("CaseTest")
    def test_02(self):
        print('this is case02')
    def tearDown(self):
        print('this is teardown')
    @classmethod
    def tearDownClass(cls):
        print('this is class teardown')

def get_suite(i):
    '''
    设计testcase执行顺序，以及生成报告
    :param i:
    :return:
    '''
    print('get_suite里面的', i)
    suite = unittest.TestSuite()
    suite.addTest(CaseTest('test_02', i))
    # suite.addTest(CaseTest('test_01', parame = i))
    # unittest.TextTestRunner().run(suite)
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

if __name__ == '__main__':
    # print('启动appium')
    # appium_init()
    threads = []
    print('在什么情况？')
    for i in range(2):       # for i in range(get_count())
        print("i:",i)
        # t = threading.Thread(target=get_suite, args=(i,))  # 注意args=(i,)要加上逗号
        t = multiprocessing.Process(target=get_suite, args=(i,))
        threads.append(t)
        print('threads:', threads)
        # t.start()
    for j in threads:
        j.start()
        time.sleep(2)