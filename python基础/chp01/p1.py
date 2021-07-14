#!/usr/bin/env python
# coding:utf8
# ------------------------
__time__ = '2021/5/16 12:22'
__author__ = 'Liang'

# ------------------------
import chp02

a = 100
b = '小小'

__all__ = ["b"]  # 引入包的时候只能让外部访问 b  仅限于from chp01.p1 import *  方式


def testDemo():
    print("hi test")
