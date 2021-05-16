#!/usr/bin/env python
# coding:utf8
# ------------------------
__time__ = '2021/5/15 23:26'
__author__ = 'Liang'


# ------------------------


class Father:
    name = ''
    age = 33
    like = ''

    def __init__(self, name, age, like):
        self.name = name
        self.age = age
        self.like = like

    def work(self):
        print(self.name+"正在上班,我喜欢"+self.like)


