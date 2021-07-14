#!/usr/bin/env python
# coding:utf8
"""
__time__ = '2021/6/18 14:32'
__author__ = 'Liang'
"""

import requests
from bs4 import BeautifulSoup
import os


url = "https://www.mzitu.com/"
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/86.0.4240.198 Safari/537.36'}
re = requests.get(url, headers=headers)
soup = BeautifulSoup(re.text, 'html.parser')
html = soup.prettify()
print(html)
