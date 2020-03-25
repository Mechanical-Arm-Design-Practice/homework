n = input('n=')
n = int(n)
print("for loop:")
for i in range(1, n+1):
    for j in range(1, n+1):
        # print(i,j)
        print(i, "*", j, "=", i*j)

print("while loop:")
a = 1
while(a <= n):
    b = 12
    while(b <= n):
        print(a, "*", b, "=", a*b)
        b += 1
    a += 1
 