#!/usr/bin/env python
# coding:utf8
"""
__time__ = '2021/6/18 9:19'
__author__ = 'Liang'

整合爬取图片

"""
import requests
from bs4 import BeautifulSoup
import os




class MZITU:
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/86.0.4240.198 Safari/537.36'}

    def get_alt_url(self, pm_soup):
        """
        查找主页图片链接
        """

        alt_url_arr = []
        alt_url_tag = pm_soup.find_all('a', target="_blank")  # alt 链接
        for img_url in alt_url_tag:
            #  数据去重
            href_url = img_url.get('href')
            if href_url not in alt_url_arr:
                alt_url_arr.append(href_url)
        return alt_url_arr

    def get_alt_name(self, pm_soup):
        """
        查找主页图片名字
        """

        alt_name_arr = []
        img_name = pm_soup.select("a > img")  # alt 名字
        for alt_name in img_name:
            alt_name_arr.append(alt_name.get('alt'))
        return alt_name_arr

    def get_num_pags(self, pm_url):
        """

        获取页数
        参数
        pm_url 二级链接地址
        """

        response = requests.get(pm_url, headers=self.headers)
        temp_soup = BeautifulSoup(response.text, 'html.parser')
        # html = temp_soup.prettify()
        #  获取图片组的页数 48 页
        span_soup = temp_soup.select("a > span")
        num = 0
        for i in span_soup:
            if num == 4:
                return i.string
            num += 1

    def creat_dic(self, pm_alt_name_arr, pm_alt_url_arr_new):
        """
        创建一个字典保存 名字和链接
        参数
        pm_alt_name_arr 图片名字数组
        pm_alt_url_arr_new 图片链接数组
        """

        pic_dit = {}
        #  根据图片个数截取链接个数
        for i in range(0, len(pm_alt_name_arr)):
            key = pm_alt_name_arr[i]
            value = pm_alt_url_arr_new[i]
            pic_dit[key] = value
        return pic_dit

    def down_img(self, pm_img_url, pm_dir_name):
        """
         下载图片
         参数：
         pm_img_url 图片地址
         pm_dir_name 传入保存图片路径名  D:\liang\PycharmProjects\pythonProject\爬虫\*.jpg'
         """
        re = requests.get(pm_img_url, headers=self.headers)
        soup = BeautifulSoup(re.text, 'html.parser')
        html = soup.prettify()
        img_url = soup.find('img', class_='blur').get('src')
        with open(pm_dir_name, 'wb') as f:
            img = requests.get(img_url, headers=self.headers)
            f.write(img.content)
            print("【图片】" + pm_dir_name + "下载完成")


if __name__ == '__main__':
    # https: // www.mzitu.com /
    url = "https://www.xxsy.net/"
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/86.0.4240.198 Safari/537.36'}
    re = requests.get(url, headers=headers)
    soup = BeautifulSoup(re.text, 'html.parser')
    html = soup.prettify()
    print(html)

    mzitu_instance = MZITU()
    name_arr = mzitu_instance.get_alt_name(soup)
    url_arr = mzitu_instance.get_alt_url(soup)
    print(url_arr, len(url_arr))
    print(name_arr, len(name_arr))
    dic = mzitu_instance.creat_dic(name_arr, url_arr)
    print(dic)
    sav_path = os.getcwd()
    print(sav_path)
