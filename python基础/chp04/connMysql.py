#!/usr/bin/env python
# coding:utf8
# ------------------------
# 连接Mysql
__time__ = '2021/5/18 22:45'
__author__ = 'Liang'

# ------------------------
import mysql.connector as conn

mydb = conn.connect(
    host="47.98.101.50",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="lbwnb123",  # 数据库密码
    database="mysql"  # 表示要使用那个库
)

print(mydb)
mycursor = mydb.cursor()  # 数据库游标

# mycursor.execute("create database test") #创建数据库
# mycursor.execute("show DATABASES") # 遍历游标取出所有的库
# for i in mycursor:
#     print(i)

# mycursor.execute("create table liang(id int,name varchar(10))")


