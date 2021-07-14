#!/usr/bin/env python
# coding:utf8
"""
__time__ = '2021/6/17 15:55'
__author__ = 'Liang'
"""
import requests
from bs4 import BeautifulSoup
import os


def obj(old_arr):
    new_arr = []
    for i in old_arr:
        if i not in new_arr:
            new_arr.append(i)
    return new_arr


def dow_img(dir_path, img_url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/86.0.4240.198 Safari/537.36'}
    re = requests.get(url, headers=headers)
    soup = BeautifulSoup(re.text, 'html.parser')
    html = soup.prettify()
    img_url = soup.find('img', class_='blur').get('src')

    num = 0

    with open(dir_path + str(num) + '.jpg', 'wb') as f:
        img = requests.get(img_url, headers=headers)
        f.write(img.content)
        num += 1
        print('下载第' + str(num) + '张图片')


url = "https://www.mzitu.com/"
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/86.0.4240.198 Safari/537.36'}
re = requests.get(url, headers=headers)
soup = BeautifulSoup(re.text, 'html.parser')
html = soup.prettify()
print(html)

"""查找名字"""
imgname = soup.select("a > img")  # alt 名字
alt_name_arr = []
alt_url_arr = []
alt_url_arr_new = []
for altname in imgname:
    alt_name_arr.append(altname.get('alt'))

"""查找链接"""
url = soup.find_all('a', target="_blank")  # alt 链接
for alt_url in url:
    alt_url_arr.append(alt_url.get('href'))

alt_url_arr_new = obj(alt_url_arr)

# print(alt_url_arr_new)
# print(len(alt_url_arr_new))

for name in alt_name_arr:
    print(name)
print(len(alt_name_arr))

for url in alt_url_arr_new:
    print(url)
print(len(alt_url_arr_new))

# 创建一个字典保存 名字和链接
pic_dit = {}
for i in range(0, len(alt_name_arr)):
    key = alt_name_arr[i]
    value = alt_url_arr_new[i]
    pic_dit[key] = value

print(pic_dit)
# print(os.getcwd())


for i in pic_dit:
    #  创建文件目录
    dir_name = i
    os.mkdir(os.getcwd() + "/" + dir_name)
    # 打开链接下载图片
    url = pic_dit[i]
    dir_path = os.getcwd() + "/" + dir_name + "/"
    print("正在的图片组为：" + dir_name)
    print("正在下载的图片地址为：" + url)
    if "https://www.mzitu.com/app/" != url:
        dow_img(dir_path, url)
