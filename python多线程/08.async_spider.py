#!/usr/bin/env python
# coding:utf8
"""
__time__ = '2021/6/22 15:43'
__author__ = 'Liang'
"""

import asyncio
import time

import aiohttp
import blog_spider

# 定义协程
# async 定义一个协程
# await 当现场执行到这里时 不进行阻塞 继续下一个程序的执行
# async with 定义一个异步的对象

async def async_craw(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            result = await resp.text()
        print(f"craw url:{url},{len(result)}")

# 获取事件循环
loop = asyncio.get_event_loop()

# 创建task任务列表
tasks = [
    loop.create_task(async_craw(url))
    for url in blog_spider.urls

]
start = time.time()
# 执行爬虫事件列表
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
print("use time seconds: ", end - start)