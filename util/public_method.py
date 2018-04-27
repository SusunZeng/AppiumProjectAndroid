#coding=utf-8
'''
类名:public_method.py
类作用:封装函数,有get_driver(),get_size(),swipe_left(),swipe_right(),swip_up(),swip_down(),swipe_on(),login()等
      调用login_page的driver
作者：曾志坤，时间：20180315
'''
# from util.devices_init import Devices_Init
# from base.base_driver import BaseDriver

class Public_Method:
    def __init__(self,driver):
        # base_driver = BaseDriver()
        # self.driver = base_driver.android_driver(driver)
        self.driver = driver
        # print('driver值：',self.driver)

    def get_size(self):
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
        return width, height

    def swipe_left(self,t):
        '''
        函数名：swipe_left(t)
        函数作用：向左边滑动，t:滑动时间，越大滑动越慢
        作者：曾志坤，时间：20180314
        '''
        # [100,200]
        x1 = self.get_size()[0] / 10 * 9
        y1 = self.get_size()[1] / 2
        x = self.get_size()[0] / 10
        self.driver.swipe(x1, y1, x, y1, t)


    def swipe_right(self,t):
        '''
        函数名：swipe_right(t)
        函数作用：向右边滑动，t:滑动时间，越大滑动越慢
        作者：曾志坤，时间：20180314
        '''

        # [100,200]
        x1 = self.get_size()[0] / 10
        y1 = self.get_size()[1] / 2
        x = self.get_size()[0] / 10 * 9
        self.driver.swipe(x1, y1, x, y1, t)

    def swipe_up(self,t):
        '''
        函数名：swipe_up(t)
        函数作用：向上滑动，t:滑动时间，越大滑动越慢
        作者：曾志坤，时间：20180314
        '''
        # [100,200]
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10 * 9
        y = self.get_size()[1] / 10
        self.driver.swipe(x1, y1, x1, y, t)

    def swipe_down(self,t):
        '''
        函数名：swipe_down(t)
        函数作用：向下滑动，t:滑动时间，越大滑动越慢
        作者：曾志坤，时间：20180314
        '''
        # [100,200]
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10
        y = self.get_size()[1] / 10 * 9
        self.driver.swipe(x1, y1, x1, y, t)


    def swipe_on(self,direction, t):

        '''
        函数名：swipe_on(direction, t)
        函数作用：汇总向左向右向上向下的滑动函数，只需要输入滑动的方向
        作者：曾志坤，时间：20180314
        '''
        if direction == 'up':
            self.swipe_up(t)
        elif direction == 'down':
            self.swipe_down(t)
        elif direction == 'left':
            self.swipe_left(t)
        else:
            self.swipe_right(t)



