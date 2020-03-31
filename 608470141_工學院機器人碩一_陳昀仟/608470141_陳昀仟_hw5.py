#!/usr/bin/env python
#-*-coding:UTF-8 -*-

# 試寫一個名為Student 的類別
# 其中屬性包含:
# name, gender, grades
# 函數包含:
# avg: 回傳grades list的平均值
# add(grade): 新增成績到grades list中
# fcount: 回傳不及格(<60)的總數
# 分別將每個學生的成績平均、不及格的的數目印出
# 寫一個名為top的類別函數:
# 傳入值為多個學生物件(使用不定個數)
# 將平均分數最高的學生回傳


class Student():
    def __init__(self):
        self.name = ""
        self.gender = ""
        self.grades = []

    def avg(self):
        tmp = 0.0
        if len(self.grades) != 0:
            for i in self.grades:
                tmp += float(i)/len(self.grades)
            print(tmp)
        else:
            print("Do not make jokes,grades is empty")

    def add(self,grade):
        self.grades.append(grade)

    def fcount(self)

a = Student()

a.avg()
