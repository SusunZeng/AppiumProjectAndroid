#coding=utf-8
'''
文件名：clear_edit_text.py
作用：清空文本框、获取要删除的文本框内容、删除文本框内容、检查文本框是否删除成功
参考：https://www.cnblogs.com/syw20170419/p/8392458.html
作者：曾志坤，时间：20180404
'''

class ClearEditText:
    def __init__(self,driver):
        self.driver = driver
        print('driver值：',self.driver)

    def clean_txt(self,text):
        '''
        清空文本框方法的封装
        :param text:
        :return:
        '''
        self.driver.keyevent(123)   #123代表光标移动到末尾键
        for i in range(0,len(text)):
            self.driver.keyevent(67)    #67退格键

    def find_txt(self,id):
        '''
        获取到要删除的文本框内容
        :param id:
        :return:
        '''
        find_txt = self.driver.find_element_by_id(id)
        find_txt.click()
        print('文本框内容：',find_txt.get_attribute('text'))
        return find_txt.get_attribute('text')

    def delete_text(self,id):
        '''
        删除文本框内容
        :return:
        '''
        get_text = self.find_txt(id)
        self.driver.clean_text(get_text)

    def check_Delete(self,id):
        '''
        检查文本框是否删除成功
        :return:
        '''
        get_text = self.find_txt(id)
        if get_text == "":
            print("文本框删除成功")
        else:
            print("文本框删除失败")

# if __name__ == "__main__":
#         clear_edit_text = ClearEditText(self.driver)
#         c =study()
#         c.find_ele('id/ajdha')
#         c.Delete()
#         c.check_Delete()

