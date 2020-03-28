print("\n====9*9 Multiplication Table====")

#Homework2:[For]
print("\n====Homework2: [For]====")
print("Enter n = (n>1)")
n = int(input())
while(n<1):
    print("Error! n should be larger than 1.")
    print("\nPlease enter n = (n>1)")
    n=int(input())
    if(n>1):
        break

for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,"*",j,"=",i*j)

#Homework2:[While]
print("\n====Homework2: [While]====")
print("Enter n = (n>1)")
nn = int(input())
while(nn<1):
    print("Error! n should be larger than 1.")
    print("\nPlease enter n = (n>1)")
    nn=int(input())
    if(nn>1):
        break

iter1=1
while(iter1 <= nn):
    iter2=1
    while(iter2 <= nn):
        print(iter1,"*",iter2,"=",iter1*iter2)
        iter2+=1
    iter1+=1