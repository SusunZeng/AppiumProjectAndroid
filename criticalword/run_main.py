#coding=utf-8
'''
文件：run_main.py
作用：读取case excel表格用例步骤，来逐步执行，以及判断结果
作者：曾志坤，时间：20180327
'''
import sys
sys.path.append("E:/AppiumProjectAndroid")
from criticalword.get_data import GetData
from criticalword.action_method import ActionMethod
from util.server import Server

class RunMain:
    def run_method(self):
        sever = Server()
        sever.main()
        data = GetData()
        action_method = ActionMethod()
        lines = data.get_case_lines()
        print('行数：',lines)
        for i in range(1,lines):
            handle_step = data.get_handle_step(i)
            element_key = data.get_element_key(i)
            handle_value = data.get_handle_value(i)
            expect_key = data.get_expect_element(i)
            expect_step = data.get_expect_handle(i)

            #input()    login_button
            #input str
            #None
            excute_method = getattr(action_method, handle_step)
            if handle_value != None:
                excute_method(element_key, handle_value)  # 并不是所有输入值都是两个
            else:
                excute_method(element_key)
            if expect_step != None:
                expect_result = getattr(action_method, expect_step)
                result = expect_result(expect_key)
                if result:
                    data.write_value(i,'pass')
                else:
                    data.write_value(i,'fail')


            if expect_key != None:
                result_method = getattr(action_method,expect_key)
                result_method()


if __name__ == '__main__':
    run = RunMain()
    run.run_method()

