#!/usr/bin/env python
# coding:utf8
"""
__time__ = '2021/6/20 22:04'
__author__ = 'Liang'
生产者消费者 spider
"""
import queue
import blog_spider
import time
import threading
import random


def do_crawl(url_queue: queue.Queue, html_queue: queue.Queue):
    while True:
        url = url_queue.get()
        html = blog_spider.crawl(url)
        html_queue.put(html)
        print(threading.current_thread().name, f"craw{url}",
              "url_queue.size=", url_queue.qsize()
              )
        time.sleep(random.randint(1, 2))


def do_parse(html_queue: queue.Queue, fout):
    while True:
        html = html_queue.get()
        results = blog_spider.parse(html)
        for result in results:
            fout.write(str(result) + "\n")
        print(threading.current_thread().name, f"parse{results}",
              "html_queue.size=", html_queue.qsize()
              )
        time.sleep(random.randint(1, 2))


if __name__ == '__main__':
    url_queue = queue.Queue()
    html_queue = queue.Queue()
    for url in blog_spider.urls:
        url_queue.put(url)

    # 启动3个生产者线程
    for idx in range(20):
        t = threading.Thread(target=do_crawl, args=(url_queue, html_queue),
                             name=f'craw{idx}')
        t.start()
        fout = open("02.data.txt", "w")
    # 启动3个消费者线程
    for idx in range(20):
        t = threading.Thread(
            target=do_parse, args=(html_queue, fout),
            name=f"parse{idx}"
        )
        t.start()

