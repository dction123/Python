#!/usr/bin/env python
# coding:utf8
"""
__time__ = '2021/6/20 21:14'
__author__ = 'Liang'
"""
import blog_spider
import threading
import time


def single_thread():
    print("single_thread begin")
    for url in blog_spider.urls:
        blog_spider.crawl(url)
    print("single_thread end")


def multi_thread():
    print("multi_thread begin")
    threads = []
    for url in blog_spider.urls:
        threads.append(
            # args 传入的是元组 所以为 (url,)
            threading.Thread(target=blog_spider.crawl, args=(url,))
        )

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    print("multi_thread end")


if __name__ == "__main__":
    start_time = time.time()
    single_thread()
    end_time = time.time()
    print("single_thread cost:%s", end_time - start_time, "seconds")

    start_time = time.time()
    multi_thread()
    end_time = time.time()
    print("multi_thread cost:%s", end_time - start_time, "seconds")
