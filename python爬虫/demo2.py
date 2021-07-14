#!/usr/bin/env python
# coding:utf8
"""
__time__ = '2021/6/17 15:30'
__author__ = 'Liang'
"""
import requests
from bs4 import BeautifulSoup


def dow_pic(url_path):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/86.0.4240.198 Safari/537.36'}
    re = requests.get(url, headers=headers)
    soup = BeautifulSoup(re.text, 'html.parser')
    img_path = soup.find_all('img', class_='lazy')
    # print(img_path)
    print(len(img_path))
    print(type(img_path))
    num = 0
    for link in img_path:
        print()
        with open(str(num) + '.jpg', 'wb') as f:
            img = requests.get(link.get('data-original'), headers=headers)
            f.write(img.content)
            num += 1
            print('下载第' + str(num) + '张图片')


if __name__ == '__main__':
    url = "https://www.mzitu.com/zipai/"
    dow_pic(url)
