#!/usr/bin/env python
# coding:utf8
# ------------------------
__time__ = '2021/5/15 22:53'
__author__ = 'Liang'
# ------------------------
"""
面向对象练习
构造方法 类属性 普通方法
私有方法 私有属性
"""

people = 10000  # 全局变量


class ClassDemo:
    __address = '四川成都'  # 私有属性
    _country = 'China'  # 受保护的属性

    def __init__(self, name, age):  # 构造方法
        self.name = name
        self.age = age
        print("我是构造方法")
        print("我的名字是：", self.name)
        print("我的年龄是：", self.age)
        print(self.__address)
        print(self._country)
        global people
        people = 222
        print(people)

    def __siyou(self):
        print("私有方法")

    def say(self):  # 方法
        print(self.name + "正在说")
        self.__siyou()  # 通过self.的形式调用私有方法 只能在类中调用

    @classmethod
    def classFunction(cls):
        print("我是类方法")


test = ClassDemo('张三', 10)
# test.say()
ClassDemo.classFunction()
