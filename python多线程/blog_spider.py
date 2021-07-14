#!/usr/bin/env python
# coding:utf8
"""
__time__ = '2021/6/20 21:04'
__author__ = 'Liang'
博客园spider
"""


import requests
from bs4 import BeautifulSoup

urls = [f"https://www.cnblogs.com/sitehome/p/{page}"
        for page in range(1, 50 + 1)]


def crawl(url):
    r = requests.get(url)
    # print(url, len(r.text))
    return r.text


def parse(html):
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a", class_="post-item-title")
    return [(link["href"], link.get_text()) for link in links]


