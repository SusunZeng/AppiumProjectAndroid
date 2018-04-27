#coding=utf-8

from util.server import Server
from base.base_driver import BaseDriver
import time

class Devices_Init:
    def __init__(self):
        self.server = Server()
        self.baseDriver = BaseDriver()

    def devices_appium_init(self):
        self.server.main()
        self.baseDriver.android_driver(0)
        time.sleep(20)
#
if __name__ == '__main__':
    devices_init = Devices_Init()
    print(devices_init.devices_appium_init())