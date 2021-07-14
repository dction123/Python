#!/usr/bin/env python
# coding:utf8
"""
__time__ = '2021/6/21 23:37'
__author__ = 'Liang'
线程池的使用
concurrent.futures.ThreadPoolExecutor()
map 的使用
submit 的使用


"""

import concurrent.futures
import blog_spider

# craw
with concurrent.futures.ThreadPoolExecutor() as pool:
    # map 拿到所有的结果并以列表的形式返回
    # map 传入一个已经准备好的参数列表
    htmls = pool.map(blog_spider.crawl, blog_spider.urls)

    htmls = list(zip(blog_spider.urls, htmls))
    for url, html in htmls:
        print(url, len(html))

print("craw over")

# parse
# map 和 submit 都是在线程执行完毕后  再依次返回结果 都是按顺序返回
# map 的返回结果是一个列表
# submit 的返回结果是 future 通过future.result()方法返回结果
with concurrent.futures.ThreadPoolExecutor() as pool:
    futures = {}

    for url, html in htmls:
        future = pool.submit(blog_spider.parse, html)
        futures[future] = url

    # 获取结果的第一种方式 future.result

    # for future,url in futures.items():
    #     print(url,future.result())

    # 获取结果的第二种方式 concurrent.futures.ThreadPoolExecutor.as_completed() 返回线程执行完的结果 不按顺序返回
    for future in concurrent.futures.as_completed(futures):
        url = futures[future]
        print(url, future.result())
