#coding=utf-8
'''
函数名:read_init.py
函数作用:读取配置文件代码封装,读取文件config路径下方的文件,可以在file_path修改读取文件
作者:曾志坤,时间:20180315
'''

import configparser
# read_ini = configparser.ConfigParser()
# data  = read_ini.read('E:\AppiumProjectAndroid\config\LocalElement.ini')
# print(data)
# print(read_ini.get('login_element','username'))

class ReadIni:
	def __init__(self,file_path=None):
		if file_path == None:
			self.file_path = 'E:/AppiumProjectAndroid/config/LocalElement.ini'
		else:
			self.file_path = file_path
		self.data = self.read_ini()

	def read_ini(self):
		read_ini = configparser.ConfigParser()
		read_ini.read(self.file_path)
		return read_ini

	#通过key获取对应的value
	def get_value(self,key,section=None):
		if section == None:
			section = 'login_element'

		try:
			value = self.data.get(section,key)
		except:
			value = None

		return value

if __name__ == '__main__':
	read_ini = ReadIni()
	# 读取配置文件内容
	# print('read_ini:',read_ini)
	# read_ini.get_value("username","login_element",)
	# print(read_ini.get_value("username","login_element"))
