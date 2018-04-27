#coding=utf-8
'''
文件名：driver_init.py
作用：在其他模块引用该变量时，作用跟全局变量类似，但除了登录相关模块的以外，其他模块都不能在__init__方法里面应用
作者：曾志坤，时间：20180412
指导：崔琳聪
'''

class DriverInit:
    driverInit = None
