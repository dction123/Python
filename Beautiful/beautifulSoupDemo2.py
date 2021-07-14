#!/usr/bin/env python
# coding:utf8
"""__time__ = '2021/6/15 13:06'
__author__ = 'Liang'

对象的种类 演示
Tag
Name
Attributes
"""
from bs4 import BeautifulSoup
from lxml.html.clean import unicode

soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', "html.parser")
tag = soup.b
print("-" * 15 + "tag" + "-" * 15)
print("tag.type:", type(tag))
print("tag:", tag)
print("tag.text:", tag.text)
print("tag.name:", tag.name)
print("-" * 15 + "Attributes" + "-" * 15)
print(tag['class'])
print(tag.attrs)

'''
tag的属性可以被添加,删除或修改
'''
print(tag['class'])
tag['class'] = 'liang'  # 修改tag
print(tag['class'])
print(tag)
tag['id'] = 'id1'  # 修改id
print(tag)

del tag['class']  # 删除class
print(tag)

del tag['id']  # 删除id
print(tag)

"""
多值属性
"""
print("-" * 15 + "多值属性" + "-" * 15)
css_soup = BeautifulSoup('<p class="body strikeout"></p>', "html.parser")
print(css_soup.p['class'])  # 多值属性会被以list形式显示

rel_soup = BeautifulSoup("<a>hello World</a>", "html.parser")  # 修改多值属性
print(rel_soup)
rel_soup.a['ref'] = ['test', 'demo']
print(rel_soup)

xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'xml')  # xml格式不包含多值属性
print(xml_soup.p['class'])

"""
可以遍历的字符串
Beautiful Soup用 NavigableString 类来包装tag中的字符串
NavigableString对象转换成Unicode
replace_with() tag中包含的字符串不能编辑,但是可以被替换成其它的字符串
"""
print("-" * 15 + "可以遍历的字符串" + "-" * 15)
print(tag)
print(type(tag.string))

unicode_string = unicode(tag.string)
print(type(unicode_string))

print(tag)
tag.string.replace_with('我是被替换后的tag内容')
print(tag)
