#coding=utf-8
'''
多线程
'''
import threading
def sum(a):
    print(a+1)
threads = []
for i in range(3):
    print(i)
    t = threading.Thread(target=sum,args=(i,))  #注意args=(i,)要加上逗号
    threads.append(t)
    print('threads:',threads)
    # t.start()
for j in threads:
    j.start()
