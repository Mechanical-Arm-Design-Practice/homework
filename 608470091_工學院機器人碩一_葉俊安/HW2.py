n = int(input("n : "))

print('\nfor 迴圈:')
for i in range(1,n+1):
    for j in range(1,n+1):
     print(i,'X',j,'=',i*j)


print('\nwhile 迴圈:')
x = 0
y = 0 
while x <= n-1: 
    x += 1 
    y = 0
    while y <= n-1:
        y += 1
        print(x,'*',y,'=',x*y)
