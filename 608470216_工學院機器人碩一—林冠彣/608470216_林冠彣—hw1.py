print("-------------Q1------------")
math = {"Tom","John","Mary","Jimmy","Sunny","Amy"}
english = {"John","Mary","Tony","Bob","Pony","Tom","Alice"}

print("math is pass but failed in english : (%s) " %(math-english))
print('english is pass but failed in math : (%s)' %(english-math))
print('all pass : (%s)' %(math&english))
print('class : (%d)' %len(math.union(english)))

print("-------------Q2------------")
tom = [80,100,90,95]
john = [100,93,75,80] 
information = {"Tom":tom,"John":john}
Tomavg = sum(information['Tom']) / len(tom)
johnavg = sum(information['John']) / len(john)
print("Tom's avg : %d , John's avg : %d" %(Tomavg ,johnavg))
