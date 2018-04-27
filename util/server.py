#coding=utf-8
'''
作用：获取设备真正信息
作者：曾志坤，时间：20180319/20
'''
from util.dos_cmd import DosCmd
from util.port import Port
import threading
from util.write_user_command import WriteUserCommand
import time
class Server:
    def __init__(self):
        self.dos = DosCmd()
        self.devices_list = self.get_devices()
        self.write_file = WriteUserCommand()

    def get_devices(self):
        '''
        获取设备信息
        :return:
        '''
        devices_list = []
        result_list = self.dos.excute_cmd_result('adb devices')
        print('result_list:', result_list)
        #代表最低有个设备信息
        if len(result_list)>=2:
            for i in result_list:
                if 'List' in i:
                    continue
                devices_info = i.split('\t')    #devices信息自带有个\t
                if devices_info[1] == 'device':
                    devices_list.append(devices_info)
            return devices_list
        else:
            return None
    def create_port_list(self,start_port):
        '''
        创建可用端口
        :return:
        '''
        port = Port()
        port_list = []
        port_list = port.create_port_list(start_port,self.devices_list)
        return port_list

    def create_command_list(self,i):
        '''
        生成命令
        # appium -p 4700 -bp 4701 -U 127.0.0.1:21503
        command_list = []
        :return:
        '''

        command_list = []
        appium_port_list = self.create_port_list(4700)
        bootstrap_port_list = self.create_port_list(4900)
        device_list = self.devices_list
        print('i:',i)
        print('device_list:',device_list[i][0])
        # for i in range(len(device_list)): #直接在方法名传入i，使用的是多进程方法
        command = 'appium -p '+ str(appium_port_list[i]) +' -bp '+ str(bootstrap_port_list[i]) +' -U '+ str(device_list[i][0])+' --no-reset --session-override --log E:\\AppiumProjectAndroid\\log\\test01.log'
        command_list.append(command)
        self.write_file.write_data(i, str(device_list[i][0]), str(bootstrap_port_list[i]), str(appium_port_list[i]))
        return command_list

    def start_sever(self,i):
        '''
        启动appium服务，在终端输入命令
        :return:
        '''
        self.start_list = self.create_command_list(i)
        print('self.start_list:',self.start_list)
        self.dos.excute_cmd(self.start_list[0])

    def kill_server(self):
        '''
        杀掉appium进程，清理appium环境
        :return:
        '''
        server_list = self.dos.excute_cmd_result('tasklist | find "node.exe"')
        print('server_list:',server_list)
        if len(server_list)>0:
            # self.dos.excute_cmd('taskkill -F -PID node.exe')    #老师范例，使用打开cmd终端，但不输出结果
            command01 = self.dos.excute_cmd_result('taskkill -F -PID node.exe')
            print('终端输入命令：',command01)

    def main(self):
        '''
        多线程启动appium
        :return:
        '''
        thread_list = []
        self.kill_server()
        self.write_file.clear_data()
        for i in range(len(self.devices_list)):
            appium_start = threading.Thread(target=self.start_sever,args=(i,))
            thread_list.append(appium_start)
            print('thread_list:',thread_list)
            appium_start.start()
        # for j in thread_list:
        #     j.start()
        time.sleep(25)

if __name__ == '__main__':

    server = Server()
    print(server.main())





