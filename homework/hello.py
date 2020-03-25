print('\n###result###')
print('-----for-----')
n=input('input number n (n>1) : ')
for i in range(1,int(n)+1):
    for j in range(1,int(n)+1):
        c=i*j
        print(i,'*',j,'=',c)
print('')

print('-----while-----')
n_=input('input number n (n>1) : ')
n=int(n_)
i=j=15
while(1):
    c=i*j
    print(i,'*',j,'=',c)
    j+=1
    if(j>n):
        i+=1
        j=1
        if(i>n):
            break
  
  