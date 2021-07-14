#!/usr/bin/env python
# coding:utf8
"""__time__ = '2021/6/15 13:06'
__author__ = 'Liang'

注释及特殊字符串
CData
CData , ProcessingInstruction , Declaration , Doctype .与 Comment 对象类似,这些类都是 NavigableString 的子类
"""
from bs4 import BeautifulSoup
from bs4 import CData
markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup, "html.parser")
comment = soup.b.string
print(comment)
print(type(comment))
print(soup.b.prettify())  # 当comment 当做html时 Comment 对象会使用特殊的格式输出:


cdata = CData("A CDATA block")
comment.replace_with(cdata)

print(soup.b.prettify())