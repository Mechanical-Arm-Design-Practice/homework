print("---------for---------")
n = input('Enter the number : ') 
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        print(" %d * %d = %d" %(i,j,i*j))

print("---------while---------")
count = 1 
while count < n+1 :
    count1 = 1
    while count1 < n+1 :
        print(" %d * %d = %d" %(count,count1,count*count1))
        count1 = count1 + 1
    count = count+1
else :
    print("over")   