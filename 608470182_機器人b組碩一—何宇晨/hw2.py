num = int(input('請輸入一個數字：'))
for i in range(1,num+1):
    for n in range(1,num+1):
        print('%s X %s ='%(i,n) ,i*n)


        #while寫法
num = int(input('請輸入一個數字：'))
n = 1
k = 1
while n < num + 1 :
    while k < num + 1 :
        print(n,'X',k,'=',n*k)
        k += 1
    n += 1
    k = 1