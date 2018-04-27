#coding=utf-8
'''
函数名:get_by_local.py
函数作用:定位信息封装,读取配置文件的所登记定位要素
作者:曾志坤,时间:20180315
'''

from util.read_init import ReadIni
from base.driver_init import DriverInit
class GetByLocal:
    def __init__(self,driver):
        self.driver = driver

    def get_element(self,key,section):
        # self.driver = DriverInit.driverInit
        # id > com.gdnybank.m: id / m_combin_edit
        read_ini =  ReadIni()
        local = read_ini.get_value(key,section)
        # print('local:',local)
        if local != None:
            by = local.split('>')[0]
            # print('by:',by)
            local_by = local.split('>')[1]
            # print('local_by:',local_by)
            try:
                if by == 'id':
                    return self.driver.find_element_by_id(local_by)
                elif by == 'ids':
                    return self.driver.find_elements_by_id(local_by)[1]     #在多个信息都是同一个元素时，使用ids时，代表选择第二个，第一个选择默认
                elif by == 'id_elements':
                    return self.driver.find_elements_by_id(local_by)
                elif by == 'className':
                    return self.driver.find_element_by_class_name(local_by)
                elif by == 'classNames':
                    return self.driver.find_elements_by_class_name(local_by)
                elif by == 'name':
                    return self.driver.find_elements_by_android_uiautomator(local_by)
                # self.device.find_element_by_android_uiautomator('text(\"' + name + '\")').click()
                else:
                    return self.driver.find_element_by_xpath(local_by)
            except:
                # self.driver.save_screenshot('../jpg/test01.png')
                return None
        else:
            return None

if __name__ == '__main__':
    get_by_local = GetByLocal()
    print(get_by_local.get_element('right_login_head','login_element'))

