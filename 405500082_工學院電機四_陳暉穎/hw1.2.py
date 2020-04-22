d ={'Tom':[80,100,90,95],'John':[100,93,75,80]}
x = d['Tom']
sum = 0
for i in range(len(d['Tom'])):
    sum+=x[i]
avg=sum/len(d['Tom'])
print("the averge score of Tom is",avg)

x = d['John']
sum = 0
for i in range(len(d['John'])):
    sum+=x[i]
avg=sum/len(d['John'])
print("the averge score of John is",avg)

