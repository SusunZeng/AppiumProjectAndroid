# !D:\Python\python.exe
# coding=utf-8

'''
类名:start_appium.py
类作用:封装函数,有get_dricer(),get_size(),swipe_left(),swipe_right(),swip_up(),swip_down(),swipe_on(),login()等
作者：曾志坤，时间：20180315
'''
import sys
import importlib
importlib.reload(sys)
sys.path.append("E:\AppiumProjectAndroid")
from appium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# 使用正则表达式筛选设备 id
import re
import os
import time
from util.get_by_local import  GetByLocal

'''
函数名：get_driver()
作用：封装启动在手机上的apk功能，自动获取手机设备序列号deviceid和系统版本号deviceVersion
作者：曾志坤，时间：20180314
'''
def get_driver():

    # 测试的包的路径和包名
    # appLocation = "E:\\AppiumProjectAndroid\\config\\nymbs2.4.00_01301721_auto.apk"
    # 读取设备 id  序列号
    readDeviceId = list(os.popen('adb devices').readlines())
    print("序列号数组：", readDeviceId)
    # 正则表达式匹配出 id 信息
    deviceId = re.findall(r'^\w*\b', readDeviceId[1])[0]
    print("序列号:", deviceId)
    # 读取设备系统版本号
    deviceAndroidVersion = list(os.popen('adb shell getprop ro.build.version.release').readlines())
    deviceVersion = re.findall(r'^\w*\b', deviceAndroidVersion[0])[0]
    print(deviceAndroidVersion)
    print(deviceVersion)

    desired_caps = {
        'platformName': 'Android',
        'platformVersion': deviceVersion,
        'deviceName': deviceId,

        # APK包名
        'appPackage': 'com.gdnybank.m',
        # APK的launcherActivity
        'appActivity': 'com.gdnybank.m.biz.LoadingActivity',
        # 添加以下两个参数即可屏蔽手机软键盘
        'unicodeKeyboard': True,
        'resetKeyboard': True,
        # "noReset": "true"   #重置手机页面
    }
    driver = webdriver.Remote('http://127.0.0.1:4700/wd/hub', desired_caps)
    time.sleep(10)
    return driver

'''
函数名：get_size()
函数作用：获得机器屏幕的宽高
作者：曾志坤，时间：20180314
'''

def get_size():
    size = driver.get_window_size()
    width = size['width']
    height = size['height']
    # print("x坐标：", width)
    # print("y坐标：", height)
    return width,height
'''
函数名：swipe_left(t)
函数作用：向左边滑动，t:滑动时间，越大滑动越慢
作者：曾志坤，时间：20180314
'''
def swipe_left(t):
    # [100,200]
    x1 = get_size()[0]/10*9
    y1 = get_size()[1]/2
    x = get_size()[0]/10
    driver.swipe(x1, y1, x, y1, t)
'''
函数名：swipe_right(t)
函数作用：向右边滑动，t:滑动时间，越大滑动越慢
作者：曾志坤，时间：20180314
'''

def swipe_right(t):
    # [100,200]
    x1 = get_size()[0]/10
    y1 = get_size()[1]/2
    x = get_size()[0]/10*9
    driver.swipe(x1, y1, x, y1, t)
'''
函数名：swipe_up(t)
函数作用：向上滑动，t:滑动时间，越大滑动越慢
作者：曾志坤，时间：20180314
'''

def swipe_up(t):
    # [100,200]
    x1 = get_size()[0]/2
    y1 = get_size()[1]/10*9
    y = get_size()[1]/10
    driver.swipe(x1, y1, x1, y, t)
'''
函数名：swipe_down(t)
函数作用：向下滑动，t:滑动时间，越大滑动越慢
作者：曾志坤，时间：20180314
'''

def swipe_down(t):
    # [100,200]
    x1 = get_size()[0]/2
    y1 = get_size()[1]/10
    y = get_size()[1]/10*9
    driver.swipe(x1, y1, x1, y, t)
'''
函数名：swipe_on(direction, t)
函数作用：汇总向左向右向上向下的滑动函数，只需要输入滑动的方向
作者：曾志坤，时间：20180314
'''

def swipe_on(direction, t):
    if direction == 'up':
        swipe_up(t)
    elif direction == 'down':
        swipe_down(t)
    elif direction == 'left':
        swipe_left(t)
    else:
        swipe_right(t)


def go_login():
    print(driver.find_element_by_id('com.gdnybank.m:id/btn_login_login'))
    driver.find_element_by_id('com.gdnybank.m:id/btn_login_login').click()

'''
函数名：login_by_class()
函数作用：当登录界面有多个元素的id一致时，可以使用elements[]数组来定位哪个元素
如：登录界面username和验证码的id一样，所以使用class_name数组来取值
作者：曾志坤，时间：20180315
'''

def login_by_class():
    element = driver.find_element_by_class_name('android.widget.EditText')
    # print("element:", element)
    elements = driver.find_elements_by_class_name('android.widget.EditText')
    # print("elements:", elements)
    # 验证具体是哪个元素
    # print(elements[2].get_attribute('text'))
    return elements
    # elements[1].send_keys(code)

'''
函数名：login()
函数作用：在登录界面输入用户名/登录密码/验证码登录，在此引用GetByLocal函数的元素定位的方法，由配置文件config来控制修改登录界面的定位元素
作者：曾志坤，时间：20180315
'''

def login():

    # driver.find_element_by_id('com.gdnybank.m:id/m_combin_edit').send_keys()
    # driver.find_element_by_id("com.gdnybank.m:id/et_pwd_login").send_keys(loginPassword)
    # 直接使用定位封装的函数来定位，可以减少代码修改数量
    get_by_local = GetByLocal(driver)
    print('-->:',get_by_local)
    get_by_local.get_element('username').send_keys('15800000097')
    time.sleep(3)
    loginPassword = 'zjc135'
    get_by_local.get_element('password').click()
    get_by_local.get_element('password').send_keys(loginPassword)
    time.sleep(3)
    code = str(input("请输入图片验证码:"))
    time.sleep(5)
    # 由于username和verificationcode验证码的id是一样的，直接选择id元素来定位，会直接默认选择username
    # 以下选择取classname数组来取值
    login_by_class()[2].send_keys(code)
    get_by_local.get_element('login_button').click()

'''
函数名：login_before()
函数作用：登录前需要选择测试环境，进入成功后若有公告提示，点击确认后再选择进入登录界面
作者：曾志坤，时间：20180316
'''
def login_before():
    # 下拉选项选择测试环境
    driver.find_element_by_id("com.gdnybank.m:id/findpwd_sp_idcty").click()
    swipe_on('up',10000)
    # 拖动到对应的定位点 定位滚动列表和滚动屏幕
    time.sleep(1)
    # 选择“外网测试环境”
    driver.find_elements_by_id("android:id/text1").__getitem__(7).click()
    # 选择确认进去登陆环境
    driver.find_element_by_id("com.gdnybank.m:id/btnConfirm").click()
    # 休眠五秒等待页面加载完成
    time.sleep(5)
    keyword = '最新公告'
    announcementFlag = driver.find_element_by_class_name('android.widget.TextView').get_attribute('text')
    print('announcementFlag=', announcementFlag)
    # 如果存在最新公告信息，则判断点击确认
    if keyword in announcementFlag:
        driver.find_element_by_id('com.gdnybank.m:id/btn_confirm').click()
        # print('yes')
    # 点击右上角的人头进行登录
    driver.find_element_by_id('com.gdnybank.m:id/btn_right_head').click()
    # # 判断是否登录成功
    # welcomingSpeech = driver.find_elements_by_class_name('android.widget.TextView').__getattribute__('text')
    # print(welcomingSpeech)
    # if welcomingSpeech != '':
    #     print('用户登录成功')
    #     driver.find_element_by_id('com.gdnybank.m:id/btn_confirm_wel_dialog').click()

    def get_tost():
        time.sleep(2)
        driver.find_element_by_id('cn.com.open.mooc:id/account_edit').send_keys('18513199586')
        tost_element = ("xpath","//*[contains(@text,'请输入密码')]")
        WebDriverWait(driver,10,0.1).until(EC.presence_of_element_located(tost_element))


driver = get_driver()
print(driver)
# login_before()
# # login_by_class()
# login()




