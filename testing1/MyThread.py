#!/usr/bin/env python
# encoding: utf-8
'''
@author: lp
@file: MyThread.py
@time: 2018/12/4 16:58
@desc:
'''
import threading
import time


class MyThread(threading.Thread):
    def __init__(self, func, args,name = ''):
        threading.Thread.__init__(self)
        self.func = func
        self.args1 = args
        self.name = name

    def getResult(self):
        return self.res

    def run(self):
        print("start",self.name,"in ",threading.Thread.name," at:",time.ctime())
        self.res = self.func(*self.args1)
        print("end ",self.name,"at:",time.ctime())