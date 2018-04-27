#coding=utf-8
'''
文件名：quitLogin_page.py
作用：取有关于我的账户，即是账户详情页面所有元素信息
作者：曾志坤，时间：20180418

'''
from util.get_by_local import GetByLocal

class MyAccountPage:
    # global driver
    # 获取登录退出页面所有的页面元素信息
    def __init__(self, driver):

        self.driver = driver
        self.get_by_local = GetByLocal(self.driver)
        # print('方法名QueryTransferPage：', driver)

    def get_action_list_element(self):
        '''
        获取主页移动银行页面的功能选项element元素
        :return:
        '''
        return self.get_by_local.get_element('action_list','myAccount_element')


