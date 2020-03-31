#!/usr/bin/env python
#-*-coding:UTF-8 -*-

# 分別用for,while迴圈各寫一個nxn的乘法表,程式可以讀取使
# 用者輸入的值n, n>1 􀀀
#  輸出樣式: (n=3)

num = input('n=')
num = int(num)
print("for loop:")
for i in range(1, num+1):
    for j in range(1, num+1):
        print(i, "*", j, "=", i*j)

print("while loop:")
k = 1

while(k <= num):
    l = 1
    while(l <= num):
        print(k, "*", l, "=", k*l)
        l += 1
    k += 1
