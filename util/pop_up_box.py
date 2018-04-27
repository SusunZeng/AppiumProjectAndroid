# -*- coding: cp936 -*-
'''
文件名：pop_up_box.py
作用：弹框输入数字
参考：http://www.cnblogs.com/kaituorensheng/p/3287652.html
作者：曾志坤，时间：20180408
'''

from tkinter import *

class PopUpBox:
    def __init__(self, master=None):
        self.master=master


    def PopUPFrame(self):
        #弹出框面板
        root = Tk()
        frm = Frame(root)
        frm.pack()

        #弹出框标题
        root.title("验证码")
        root.geometry('250x100')

        #创建单行文本框
        self.var = StringVar()
        e = Entry(root, textvariable=self.var)
        self.var.set(" ")
        e.pack()

        # #向该空间内输入文本
        # self.t = Text()
        # self.t.pack()

        #创建按钮
        Button(root, text="输入完，请直接关闭弹框").pack()
        # 当执行.py 文件后，在点击按钮退出。就正常了
        # Button(root, text="press", command = root.quit).pack()
        #进入消息循环
        root.mainloop()

        return self.var.get()

# root = PopUpBox()
# root.PopUPFrame()

