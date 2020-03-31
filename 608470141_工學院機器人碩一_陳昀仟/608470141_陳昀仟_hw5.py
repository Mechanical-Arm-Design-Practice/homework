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
        return tmp

    def add(self, grade):
        [self.grades.append(i) for i in grade]
        # for i in grade:
        #     self.grades.append(i)

    def fcount(self):
        tmp = 0
        for i in self.grades:
            tmp += 1 if(i < 60) else 0
        return tmp

    @classmethod
    def top(cls, *student):
        tmp =[]
        for i in student:
            tmp.append(i.avg())
        print("最高分學生為：%s" %student[tmp.index(max(tmp))].name)

a = Student()
b = Student()
c = Student()

a.name="a"
b.name="b"
c.name="c"

a.add([100, 59, 60, 70, 80])
b.add([87, 60, 30, 10, 20])
c.add([99, 80, 10, 61, 77])

print("a平均：%.1f,不及格：%d" % (a.avg(), a.fcount()))
print("b平均：%.1f,不及格：%d" % (b.avg(), b.fcount()))
print("c平均：%.1f,不及格：%d" % (c.avg(), c.fcount()))

Student.top(a,b,c)
