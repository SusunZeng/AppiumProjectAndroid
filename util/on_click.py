# -*- coding: cp936 -*-
'''
文件名：on_click.py
作用：弹框输入数字
参考：忘记具体参考哪了
作者：曾志坤，时间：20180402
'''



from tkinter import *


# This program  shows how to make a typein box shadow a program variable.
flag = True
class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()

        self.entrythingy = Entry(self)
        self.entrythingy.pack()

        self.button = Button(self, text="输入",
                             command=self.upper)
        self.button.pack()

        # here we have the text in the entry widget tied to a variable.
        # changes in the variable are echoed in the widget and vice versa.
        # Very handy.
        # there are other Variable types. See Tkinter.py for all
        # the other variable types that can be shadowed
        self.contents = StringVar()
        self.contents.set("输入验证码")
        self.entrythingy.config(textvariable=self.contents)

        # and here we get a callback when the user hits return. we could
        # make the key that triggers the callback anything we wanted to.
        # other typical options might be <Key-Tab> or <Key> (for anything)
        self.entrythingy.bind('<Key-Return>', self.print_contents)

    def upper(self):
        # notice here, we don't actually refer to the entry box.
        # we just operate on the string variable and we
        # because it's being looked at by the entry widget, changing
        # the variable changes the entry widget display automatically.
        # the strange get/set operators are clunky, true...
        global flag
        flag = not flag
        if not flag:
            str = self.contents.get().upper()
            self.contents.set(str)
        else:
            str = self.contents.get().lower()
            self.contents.set(str)
        # print('the contents is : ', self.contents.get())
        code = self.contents.get()
        print('验证码：',code)
        return code


    def print_contents(self, event):
        print("hi. contents of entry is now ---->", self.contents.get())
#
# root = App()
# # root.master.title("验证码")
# root.mainloop()

