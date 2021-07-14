#!/usr/bin/env python
# coding:utf8
# ------------------------
__time__ = '2021/6/15 12:42'
__author__ = 'Liang'

# ------------------------
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister2" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify())

print(soup.title)
print(soup.title.text)
print(soup.p)
print(soup.p.text)
print(soup.a)
print(soup.find_all('a'))
print(soup.find(id='link1'))
print(soup.find(class_='sister2'))

# 查找文档中所有的a标签
for link in soup.find_all('a'):
    print(link.get('href'))

# 获取所有文字信息
print(soup.get_text())


