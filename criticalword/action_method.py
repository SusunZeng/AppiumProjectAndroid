#coding=utf-8
'''
文件名：action_method.py
作用：封装操作方法
作者：曾志坤，时间：20180326
'''
from util.get_by_local import GetByLocal
from base.base_driver import BaseDriver
import time
class ActionMethod:
    def __init__(self):
        base_driver = BaseDriver()
        self.driver = base_driver.android_driver(0)
        self.get_by_local = GetByLocal(self.driver)

    def input(self,*args):
        '''
        输入值
        :param element:
        :param value:
        :return:
        *args:传进来的时list->key,value
        '''
        element = self.get_by_local.get_element(args[0])
        if element == None:
            return args[0],'元素没找到'
        element.send_keys(args[1])

    def on_click(self,*args):
        '''
        元素点击
        :param elment_key:
        :return:
        '''
        element = self.get_by_local.get_element(args[0])
        if element == None:
            return args[0],'元素没找到'
        element.clcik()

    def sleep_time(self,*args):
        time.sleep(int(args[0]))        #args[0]返回的是字符串，需要转换为整数



    def get_size(self,*args):
        '''
        函数名：get_size()
        函数作用：获得机器屏幕的宽高
        作者：曾志坤，时间：20180314
        '''
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        # print("x坐标：", width)
        # print("y坐标：", height)
        return width,height

    def swipe_left(self,*args):
        '''
        函数名：swipe_left(t)
        函数作用：向左边滑动，t:滑动时间，越大滑动越慢
        作者：曾志坤，时间：20180314
        '''
        # [100,200]
        x1 = self.get_size()[0]/10*9
        y1 = self.get_size()[1]/2
        x = self.get_size()[0]/10
        self.driver.swipe(x1, y1, x, y1, 10000)


    def swipe_right(self,*args):
        '''
        函数名：swipe_right(t)
        函数作用：向右边滑动，t:滑动时间，越大滑动越慢
        作者：曾志坤，时间：20180314
        '''
        # [100,200]
        x1 = self.get_size()[0]/10
        y1 = self.get_size()[1]/2
        x = self.get_size()[0]/10*9
        self.driver.swipe(x1, y1, x, y1, 10000)


    def swipe_up(self,*args):
        '''
        函数名：swipe_right(t)
        函数作用：向右边滑动，t:滑动时间，越大滑动越慢
        作者：曾志坤，时间：20180314
        '''
        # [100,200]
        x1 = self.get_size()[0]/2
        y1 = self.get_size()[1]/10*9
        y = self.get_size()[1]/10
        self.driver.swipe(x1, y1, x1, y, 10000)


    def swipe_down(self,*args):
        '''
        函数名：swipe_down(t)
        函数作用：向下滑动，t:滑动时间，越大滑动越慢
        作者：曾志坤，时间：20180314
        '''
        # [100,200]
        x1 = self.get_size()[0]/2
        y1 = self.get_size()[1]/10
        y = self.self.get_size()[1]/10*9
        self.driver.swipe(x1, y1, x1, y, 10000)


    def swipe_on(self,direction, *args):
        '''
        函数名：swipe_on(direction, t)
        函数作用：汇总向左向右向上向下的滑动函数，只需要输入滑动的方向
        作者：曾志坤，时间：20180314
        '''
        if direction == 'up':
            self.swipe_up()
        elif direction == 'down':
            self.swipe_down()
        elif direction == 'left':
            self.swipe_left()
        else:
            self.swipe_right()

    def get_element(self,*args):
        '''
        获取元素
        :param args:
        :return: element
        '''
        element = self.get_by_local.get_element(args[0])
        if element == None:
            return None
        return element

    def combobox_click(self,*args):
        '''
        获取下拉框
        :param args:
        :return:combobox_click
        '''
        element = self.get_by_local.get_element(args[0])
        if element == None:
            return args[0],'元素没找到'
        element.clcik()

    def on_choice_click(self,*args):
        '''
        获取下拉框
        :param args:
        :return:
        '''
        element = self.get_by_local.get_element(args[0])
        if element == None:
            return args[0],'元素没找到'
        element.clcik()

    # def verification_code(self):
    #     code = str(input("请输入图片验证码:"))
    #     self.login_page.get_verification_code_element().send_keys(code)
