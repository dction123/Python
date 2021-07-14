#!/usr/bin/env python
# coding:utf8
"""
__time__ = '2021/6/22 14:02'
__author__ = 'Liang'
flask 使用ThreadPoolExeutor 实现加速
"""
import flask
import json
import time
from concurrent.futures import ThreadPoolExecutor
app = flask.Flask(__name__)
# 创建一个全局的pool
pool = ThreadPoolExecutor()


def read_file():
    time.sleep(0.2)
    return "file result"


def read_db():
    time.sleep(0.3)
    return "db result"


def read_api():
    time.sleep(0.4)
    return "api result"


@app.route("/")
def index():
    result_file = pool.submit(read_file)
    result_db = pool.submit(read_db)
    result_api = pool.submit(read_api)

    return json.dumps({
        "result_file": result_file.result(),
        "result_db": result_db.result(),
        "result_api": result_db.result()

    })


if __name__ == '__main__':
    app.run()
