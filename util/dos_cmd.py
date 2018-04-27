#coding=utf-8
'''
作用：相当于手工输入cmd查询adb devices，command：传入命令
作者：曾志坤，时间：20180319
'''
import os

class DosCmd:
    def excute_cmd_result(self,command):
        '''
        在cmd输入命令
        :param command:
        :return: result_list
        '''
        result_list = []
        result = os.popen(command).readlines()
        for i in result:
            if i == '\n':
                continue
            result_list.append(i.strip('\n'))
        return result_list
    def excute_cmd(self,command):
        '''
        打开终端
        :param command:
        :return:
        '''
        os.system(command)

if __name__ == '__main__':
    dos = DosCmd()
    print(dos.excute_cmd_result('taskkill -F -PID node.exe'))
