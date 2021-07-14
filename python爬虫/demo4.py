#!/usr/bin/env python
# coding:utf8
"""
__time__ = '2021/6/17 23:42'
__author__ = 'Liang'
"""
import os
import requests
from bs4 import BeautifulSoup

"""
根据二级链接
获取页数
"""
def get_num_pags(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/86.0.4240.198 Safari/537.36'}
    re = requests.get(url, headers=headers)
    soup = BeautifulSoup(re.text, 'html.parser')
    html = soup.prettify()
    #  获取图片组的页数 48 页
    span_soup = soup.select("a > span")
    num = 0
    for i in span_soup:
        if num == 4:
            return i.string
        num += 1


"""
下载图片
参数：
保存路径
下载地址
页数
"""
def dow_img(dir_path, img_url,page_num):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/86.0.4240.198 Safari/537.36'}
    re = requests.get(img_url, headers=headers)
    soup = BeautifulSoup(re.text, 'html.parser')
    html = soup.prettify()


    img_url = soup.find('img', class_='blur').get('src')

    with open(dir_path + str(page_num) + '.jpg', 'wb') as f:
        img = requests.get(img_url, headers=headers)
        f.write(img.content)
        print('下载第' + str(page_num) + '张图片')



if __name__ == '__main__':
    img_url = "https://www.mzitu.com/241345"
    dir_path = os.getcwd() + "/"
    pag_num = get_num_pags(img_url)
    # 拼接url
    for i in range(1,int(pag_num)):
        if i == 1:
            img_url = "https://www.mzitu.com/241345"
        else:
            img_url = "https://www.mzitu.com/241345"+"/"+str(i)
        dow_img(dir_path, img_url,i)
