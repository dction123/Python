#!/usr/bin/env python
# coding:utf8
"""
__time__ = '2021/6/17 22:31'
__author__ = 'Liang'
"""
import requests
from bs4 import BeautifulSoup
import os


def get_alt_url(pm_soup):
    alt_url_arr = []
    alt_url = pm_soup.find_all('a', target="_blank")  # alt 链接
    for img_url in alt_url:
        #  数据去重
        if img_url not in alt_url_arr:
            alt_url_arr.append(alt_url.get('href'))
    return alt_url_arr

if __name__ == '__main__':
    url = "https://www.mzitu.com/"
    print(url)
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/86.0.4240.198 Safari/537.36'}
    re = requests.get(url, headers=headers)
    print(re.text)
    soup = BeautifulSoup(re.text, 'html.parser')
    html = soup.prettify()
    print(html)
    url_arr =get_alt_url(soup)
    print(url_arr)
