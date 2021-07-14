#!/usr/bin/env python
# coding:utf8
# ------------------------
__time__ = '2021/5/17 0:22'
__author__ = 'Liang'
# ------------------------
'''
写文件
write
with :不用关心文件关闭等操作
os 文件操作模块
'''

import os

# writeStr = '人生苦短，我用python'
# fileName = 'write.txt'
#
# with open(fileName,'a',encoding='utf-8')as file: # 写入文本
#     file.write(writeStr+"\n")
#
# with open(fileName,'r',encoding='utf-8')as file:
#     print(file.readlines())

# fileNames = os.listdir(r'D:\liang')# 返回此目录下的所有文件
# for name in fileNames:
#     print(name)

# print(os.mkdir('D:\\test')) # 创建目录
print(os.stat(r'D:\liang'))
















# if __name__ == '__main__':
#     print(os.path) #os 模块路径
#     print(os.getcwd()) #当前路径
