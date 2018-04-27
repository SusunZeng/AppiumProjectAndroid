#coding=utf-8
'''
文件名：date_number.py
作用：日期转换成str，返回strnow3，用于生成文件命名区分
作者：曾志坤，时间：20180414
'''
from datetime import datetime
def DataNumber3():
    now = datetime.now()
    # print(now)
    # strnow = datetime.strftime(now,'%Y-%m-%d %H:%M:%S')
    # # print('yyyy-MM-dd hh:MM:ss：',strnow)
    # strnow1 = datetime.strftime(now,'%Y%m%d')
    # # print('yyyyMMdd：',strnow1)
    # strnow2 = datetime.strftime(now,'%Y-%m-%d')
    # print('yyyy-MM-dd：',strnow2)
    strnow3 = datetime.strftime(now,'%Y%m%d%H%M%S') #
    # print('yyyyMMddhhMMss：', strnow3)
    return strnow3

def DataNumber1():
    now = datetime.now()
    strnow1 = datetime.strftime(now,'%Y%m%d')
    # print('yyyyMMdd：',strnow1)
    # print("report" + strnow1)
    return strnow1

# DataNumber1()