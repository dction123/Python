#!/usr/bin/env python
# coding:utf8
# ------------------------
__time__ = '2021/5/15 23:32'
__author__ = 'Liang'

# ------------------------
from chp01.father import Father


class Son(Father):  # 继承Father
    like = ''

    def __init__(self, name, age, like):
        self.like = like
        super().__init__(self.name, self.age)
        print("son的构造方法")

    def work(self):  # 重写父类方法
        print(self.name + "正在学习，我喜欢"+self.like)


# son1 = Son('小张', 10, '打篮球')
# son1.work()

father1 = Father('大张', 55, '玩电脑')
father1.work()
