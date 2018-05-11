# 参考：https://blog.csdn.net/qq_18808965/article/details/72675281
#coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,TimeoutException
#from selenium.common.exceptions import   
from selenium.webdriver.support.ui import WebDriverWait # available since 
from selenium.webdriver.common.keys import Keys


from time import sleep


#需要先安装PIL模块




# pytesser提供了两种识别图片方法，通过image对象和图片地址


from pytesser3 import *


#from pytesser import pytesser
from PIL import Image


import os,time




driver = webdriver.Chrome()
print(u"加载驱动完成..")
driver.get("http://osms.sit.sf-express.com:2080/dep/index.pub")#加载页面


driver.maximize_window() # 浏览器全屏显示


print(u"最大化页面窗口完成..")


#用于截图能截取整个页面
#driver.set_window_size(1200, 900)


#print u"设置窗口尺寸为1200 * 900"


ISOTIMEFORMAT="%Y%m%d%H%M%S"
strTime = time.strftime( ISOTIMEFORMAT, time.localtime())


print(u"加载页面完成..")


time.sleep(1)


# driver.save_screenshot('E:\\pythonScript\\Codeimages\\'+strTime+'code.png')
driver.save_screenshot('E:\\\AppiumProjectAndroid\\jpg\\'+strTime+'code.png')



print(u"保存截图完成..")


#得到截取的验证码图片
#设置元素是否用户可见
result=driver.find_element_by_id("imgcode").is_displayed()


print(u"验证码属性ID imgcode 存在",result)


size=driver.find_element_by_id("imgcode").size


print(u"打印验证码图片的属性：",size)


#获取元素的文本
text=driver.find_element_by_id("imgcode").text


print(text)


location = driver.find_element_by_id("imgcode").location
print(location)


im = Image.open('E:\\AppiumProjectAndroid\\jpg\\'+strTime+'code.png')
'''
#旋转图片
fixedIm=im.rotate(270)
fixedIm.save('E:\\AppiumProjectAndroid\\jpg\\'+strTime+'rotate.png')
#旋转图片rotate
print u"旋转图片完成"
'''
left = driver.find_element_by_id("imgcode").location['x']
top = driver.find_element_by_id("imgcode").location['y']
right = driver.find_element_by_id("imgcode").location['x'] + driver.find_element_by_id("imgcode").size['width']
bottom = driver.find_element_by_id("imgcode").location['y'] + driver.find_element_by_id("imgcode").size['height']


im = im.crop((left, top, right, bottom))


print(u"保存验证码图片完成")


im.save('E:\\ppiumProjectAndroid\\jpg\\'+strTime+'screenshot.png')
#识别图片中的验证码
os.remove('E:\\AppiumProjectAndroid\\jpg\\'+strTime+'code.png')
print(u"删除截屏图片完成")
#**************************************************************************
codeimg = Image.open('E:\\AppiumProjectAndroid\\jpg\\'+strTime+'screenshot.png')
#把彩色图像转化为灰度图像。RBG转化到HSI彩色空间，采用I分量
imgry = codeimg.convert('L')
#打开图片，展示效果 imgry.show()
#二值化处理
'''
threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
out = imgry.point(table, '1')
out.show()
'''
#imt = Image.open('E:\\pythonScript\\Codeimages\\20170524140427screenshot.png')  
print(image_to_string(imgry))


print(image_file_to_string('E:\\AppiumProjectAndroid\\jpg\\'+strTime+'screenshot.png'))


imgry.show()




