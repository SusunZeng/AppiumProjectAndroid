#coding=utf-8
'''
作用：通过yaml来获取配置命令
作者：曾志坤，时间：20180320
'''
import yaml
class WriteUserCommand:
    def read_data(self):
        '''
        加载yaml数据
        :return: data
        '''
        with open('../config/userconfig.yaml') as fr:
            data = yaml.load(fr)
        return data

    def get_value(self,key,port):
        '''
        获取value,具体哪一行数据
        :key:yaml文件关键词
        :port:yaml文件具体哪个字段
        :return:value
        '''
        data = self.read_data()
        value = data[key][port]
        return value
    def write_data(self,i,device,bp,port):
        '''
        写入数据
        :return:
        '''
        data = self.join_data(i,device,bp,port)
        with open('../config/userconfig.yaml','a') as fr:
            yaml.dump(data,fr)

    def join_data(self,i,device,bp,port):
        '''
        写入文件
        :return:data
        command = 'appium -p '+ str(appium_port_list[i]) +' -bp '+ str(bootstrap_port_list[i]) +' -U '+ str(device_list[i][0])+' --no-reset --session-override'
        '''
        data = {
        'user_info_'+str(i):{
        'deviceName':device,    #设备名称，str(device_list[i][0])
        'bp':bp,    #可用末端口，str(bootstrap_port_list[i])
        'port':port #可用起始端口，str(appium_port_list[i])
        }
        }
        return data

    def clear_data(self):
        '''
        清理文件
        :return:
        '''
        with open('../config/userconfig.yaml','w') as fr:
            fr.truncate()
        fr.close()
    def get_file_lines(self):
        '''
        获取userInfo设备行数
        :return: len(data)
        '''
        data = self.read_data()
        return len(data)

# if __name__ == '__main__':
#     write_file = WriteUserCommand()
#     print(write_file.get_value('user_info_1','bp'))