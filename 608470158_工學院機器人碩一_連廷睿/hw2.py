num = input("number =")

print("for loop")
for i in range(int(num)):
	for j in range(int(num)):
		print(i+1,"*",j+1," = ",(i+1)*(j+1))

print("while loop")
i = 1
while int(num) >= i :
	j = 1
	while int(num) >= j :
		print(i,"*",j," = ",i*j)
		j += 1
	i += 1
