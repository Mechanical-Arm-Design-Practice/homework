#!/usr/bin/env python3
# HW1

math = {'Tom', 'John', 'Mary', 'Jimmy', 'Sunny', 'Amy'}
english = {'John', 'Mary' , 'Tony' , 'Bob', 'Pony', 'Tom' , 'Alice'}

a = math - english
b = english - math
c = math | english
print("list of math > english :",a)
print("list of math < english :",b)
print("number of sutudent",len(c))

Tom = [80, 100, 90, 95]; John = [100,93,75,80]
Tom_ave = sum(Tom)/ len(Tom); John_ave = sum(John)/ len(John)
print("Tom's score average :",Tom_ave,"\nJohn's score average :",John_ave)

score = {"Tom":Tom, "John":John}
score["Tom"].append(Tom_ave); score["John"].append(John_ave)
for key, value in score.items():
    print(key + "'s score average :",value[-1])