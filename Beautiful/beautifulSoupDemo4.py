#!/usr/bin/env python
# coding:utf8
"""__time__ = '2021/6/15 13:06'
__author__ = 'Liang'
遍历文档树

"""
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
    <body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
</body>
</head>
"""
soup = BeautifulSoup(html_doc, 'html.parser')

print("tag head:", soup.head)
print("tag title:", soup.title)
print("tag body.b:", soup.body.b)  # 点取属性的方式只能获得当前名字的第一个tag:
print("tag.a:", soup.a)

print(soup.find_all('a'))  # 获取所有的a标签:
# for link in soup.find_all('a'):
#     print(link.get('href'), end='\n')

print("-" * 15 + "contents" + "-" * 15)
"""
contents 
属性可以将tag的子节点以列表的方式输出
"""

head_tag = soup.head
print(head_tag)
print(head_tag.contents)

title_tag = head_tag.contents[0]
print(title_tag)

print(title_tag.contents)

print(soup.a.contents)
print("-" * 15 + "children" + "-" * 15)
"""
.children
"""
for child in soup.body.children:
    print(child)

print("-" * 15 + "descendants" + "-" * 15)
"""
descendants
属性可以对所有tag的子孙节点进行递归循环
"""

for child in soup.body.descendants:
    print(child)

print("-" * 15 + "string" + "-" * 15)
"""
string
strings 循环获取
tripped_strings 可以去除多余空白内容:
repr 将对象转化为供解释器读取的形式
"""
print(soup.title.string)

print(soup.html.string)  # 如果tag包含了多个子节点,tag就无法确定 .string 方法应该调用哪个子节点的内容,

for string in soup.html.strings:
    print(repr(string))


print("-" * 15 + "tripped_strings" + "-" * 15)
for string in soup.stripped_strings:
    print(repr(string))

print("-" * 15 + "父节点" + "-" * 15)
"""
父节点
parent
parents 可以递归得到元素的所有父辈节点
"""
title_tag = soup.title
print(title_tag)
print(title_tag.parent)
print(title_tag.string)
print(title_tag.string.parent)  # 字符串也有父节点

link = soup.a
for parent in link.parents:
    print(parent.name)

print("-" * 15 + "兄弟节点" + "-" * 15)
"""
兄弟节点
next_sibling 下一个兄弟节点
previous_sibling 前一个兄弟节点
"""

sibling_soup  = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>",'html.parser')
print(sibling_soup.prettify())
print(sibling_soup.b.next_sibling)
print(sibling_soup.c.previous_sibling)