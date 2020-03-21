#!/usr/bin/env python3
# HW2

n = int(input("請輸入整數n: ")) + 1
for i in range(1,n):
    for j in range(1,n):
        print('%d*%d = %d'%(i, j, i*j))
print('\n')
l = 1
while l < n:
    m=1
    while m < n:
         print('%d*%d = %d'%(l, m, l*m)) # \t 可以使其上下對齊
         m+=1
    l += 1