n=int(input("input n="))
print("for")
for i in range(1,n+1):
    for j in range(1,n+1):
        print("%d*%d=%d"%(i,j,i*j))
print("while")
x=1
while x<=n:
    y=1
    while y<=n:
        print("%d*%d=%d"%(x,y,x*y))
        y+=1
    x+=1

    
    
