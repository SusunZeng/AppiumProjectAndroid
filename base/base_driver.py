#coding=utf-8
import time
from appium import webdriver
from util.write_user_command import WriteUserCommand

class BaseDriver:
	def android_driver(self,i):
		print("this is android_driver:",i)
		#devices_name adb devices
		#port
		write_file = WriteUserCommand()

		devices = write_file.get_value('user_info_'+str(i),'deviceName')
		port = write_file.get_value('user_info_'+str(i),'port')
		print('devices:',devices)
		print('port:',port)
		# 读取设备系统版本号
		# deviceAndroidVersion = list(os.popen('adb shell getprop ro.build.version.release').readlines())
		# print('deviceAndroidVersion', deviceAndroidVersion)
		# deviceVersion = re.findall(r'^\w*\b', deviceAndroidVersion[0])[0]
		# print('deviceVersion',deviceVersion)

		capabilities = {
			"platformName": "Android",
			# "platformVersion": deviceVersion,  # 设备系统版本号
			"deviceName": devices,
		  	"app": "E:\\AppiumProjectAndroid\\apps\\nymbs2.4.00_01301721_auto.apk",
			"appPackage": "com.gdnybank.m",		# APK包名
			"appActivity": "com.gdnybank.m.biz.LoadingActivity",	#APK的launcherActivity
		  	#"newCommandTimeout":'180'
			'unicodeKeyboard': True,	# 添加以下两个参数即可屏蔽手机软键盘
			'resetKeyboard': True

		}
		driver = webdriver.Remote("http://127.0.0.1:" + port + "/wd/hub", capabilities)
		time.sleep(10)
		return driver

# if __name__ == '__main__':
# 	driver = BaseDriver()
# 	print('driver:',driver.android_driver(0))
