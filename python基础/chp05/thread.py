#!/usr/bin/env python
# coding:utf8
# ------------------------
# python 多线程demo
__time__ = '2021/5/21 14:52'
__author__ = 'Liang'

# ------------------------
import _thread
import time


def printTimeThread(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1

        print("%s , %s" % (threadName, time.ctime(time.time())))


try:
    _thread.start_new_thread(printTimeThread, ("thread - 1", 2))
    _thread.start_new_thread(printTimeThread, ("thread - 2", 3))


except:
    print("erro , 无法启动线程")
while 1:
    pass
