#!/usr/bin/env python
# coding:utf8
"""
__time__ = '2021/6/21 23:09'
__author__ = 'Liang'
Lock 锁
使用 包裹代码 with lock:
"""
import threading
import time

lock = threading.Lock()
class Account:
    def __init__(self, blance):
        self.blance = blance


def draw(account:Account, amount):
    with lock:
        if account.blance >= amount:
            time.sleep(0.1)
            print(threading.current_thread().name,"取钱成功")
            account.blance -= amount
            print(threading.current_thread().name,
                  "余额", account.blance)
        else:
            print(threading.current_thread().name, "取钱失败")


if __name__ == '__main__':
    account = Account(1000)

    ta = threading.Thread(target=draw, args=(account, 800))
    tb = threading.Thread(target=draw, args=(account, 800))
    ta.start()
    tb.start()