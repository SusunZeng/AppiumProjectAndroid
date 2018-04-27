#coding=utf-8
'''
文件名：press_Keycode.py
作用:调试一个个字符输入数字，比如银行卡号在输入时常会出现输错/输多/输少的情况
参考：https://testerhome.com/topics/6267
作者：曾志坤，时间：20180423
'''
class Press_Keycode:
    def __init__(self, driver):
        self.driver = driver
    # 验证使用press_Keycode方法来输入银行卡号
    def press_Keycode(self,stringInput,element):
    #将手机号字符串转化成字符数组
        input_str=(','.join(stringInput)).split(',')
        # print('input_str方法press_Keycode:', input_str)

        #通过模拟物理按键用for循环每次输入一个字符输入手机号
        for i in range(len(input_str)):
        #用press_keycode方法模拟键盘逐个字符输入
            # print('int(input_str[' + str(i) + ']:', int(input_str[i]))
            self.driver.press_keycode(int(input_str[i]) + 7)
        #通过当前输入框内内容的长度来判断前端加空格截断后是否有多输入，有则删除多输入的
            if len((element.text).replace(" ", "")) > i+1:
                self.driver.press_keycode(67)
        #保持焦点在输入框内且每次输入单个字符后，将光标置到最后
                if i == len(input_str)/2:
                    # print('len(input_str)/2:', len(input_str)/2)
                    element.click()
                    self.driver.press_keycode(123)
