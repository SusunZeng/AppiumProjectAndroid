#coding=utf-8
'''
unittes使用
'''
import unittest
class CaseTest(unittest.TestCase):
    #加上注解，在python叫容器，当有2个case的时候，是全局的，就运行一次

    @classmethod
    def setUpClass(cls):
        print('this is class')

    def setUp(self):
        print('this is setup')
    def test_01(self):
        print('this is case01')
    def test_02(self):
        print('this is case02')
    def tearDown(self):
        print('this is teardown')

    @classmethod
    def tearDownClass(cls):
        print('this is class teardown')


if __name__ == '__main__':
    unittest.main()
