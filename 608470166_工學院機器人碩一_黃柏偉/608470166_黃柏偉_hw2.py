n=int(input("輸入一個數字(n>1) "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,"*",j,"=",i*j)
print("====================================")
i=1
while i<n+1:
    j=1
    while j<n+1:
        print(i,"*",j,"=",i*j)
        j+=1
    i+=1
