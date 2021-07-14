#!/usr/bin/env python
# coding:utf8
# ------------------------
__time__ = '2021/5/16 22:42'
__author__ = 'Liang'
# ------------------------
'''
python 文件操作
r : 可读
w : 可写
a+ :可读可写
end="" print 设置不换行
'''

file = open("dbConfig.txt", 'r' ,encoding='utf-8')

# print(file.readable()) #是否可读
# print(file.writable()) #是否可写

data = file.readlines()
count =len(data)
print(count)
dataTup = {}
for i in range(5):
    if data[i].startswith('#'):
        continue
    else:
        print(data[i],end="")
        line = data[i].split('=')
        key = line[0]
        value = line[1].replace("\n","") # 将换行符替换为空
        dataTup[key] = value

print(dataTup)
# line = file.readline()
# print(line)

file.close()


