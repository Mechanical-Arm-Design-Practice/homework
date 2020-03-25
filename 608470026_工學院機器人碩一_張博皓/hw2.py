print('\n*****************hw2 begin*****************\n')
mode=input("choose while or for to compute(while = 1, for = 2)\n")
n=int(input("enter your number\n"))

if mode=='1':
	loopw = 1
	inloopw = 1
	while loopw < (n+1):
		while inloopw < (n+1):
			print(loopw,"*",inloopw,"=", loopw * inloopw)
			inloopw+=1
		inloopw = 1
		loopw+=1		
 

elif mode=='2':
	for loop in range(1,n+1):
		for inloop in range(1,n+1):
			print(loop,"*",inloop,"=", loop * inloop)
