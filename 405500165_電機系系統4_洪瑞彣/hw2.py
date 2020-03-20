print('hw2')
n = int(input("input:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        s = i*j
        print('%d*%d=%2d ' %(i, j, s), end = "")
    print("\n")
m = int(input("input:"))
i=1
while i < m+1:
    j=1
    while j < m+1:
        s = i*j
        print('%d*%d=%2d ' %(i, j, s), end = "")
        j+=1
    print("\n")
    i+=1