# -*- coding: cp936 -*-
'''
�ļ�����pop_up_box.py
���ã�������������
�ο���http://www.cnblogs.com/kaituorensheng/p/3287652.html
���ߣ���־����ʱ�䣺20180408
'''

from tkinter import *

class PopUpBox:
    def __init__(self, master=None):
        self.master=master


    def PopUPFrame(self):
        #���������
        root = Tk()
        frm = Frame(root)
        frm.pack()

        #���������
        root.title("��֤��")
        root.geometry('250x100')

        #���������ı���
        self.var = StringVar()
        e = Entry(root, textvariable=self.var)
        self.var.set(" ")
        e.pack()

        # #��ÿռ��������ı�
        # self.t = Text()
        # self.t.pack()

        #������ť
        Button(root, text="�����꣬��ֱ�ӹرյ���").pack()
        # ��ִ��.py �ļ����ڵ����ť�˳�����������
        # Button(root, text="press", command = root.quit).pack()
        #������Ϣѭ��
        root.mainloop()

        return self.var.get()

# root = PopUpBox()
# root.PopUPFrame()

