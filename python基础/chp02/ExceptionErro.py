#!/usr/bin/env python
# coding:utf8
# ------------------------
__time__ = '2021/5/16 21:32'
__author__ = 'Liang'
# ------------------------

'''
异常 处理和重写异常
raisee 主动抛出一个异常
使用 as 给异常一个别名 
else : 程序没有异常时执行的代码
'''


class MyErro(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "[%s]" % self.message


try:
    a = 10
    b = 0
    # c = a / b
    c = a + b
    raise MyErro('我是自定义的异常')

except Exception as e:
    print(type(e))
    print(e)


else:
    print("程序没有异常时执行的代码")
finally:
    print("finally 程序一定会执行的")
