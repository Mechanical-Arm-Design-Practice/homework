math = {'Tom','John','Mary','Jimmy','Sunny','Amy'}
en = {'John','Mary','Tony','Bob','Pony','Tom','Alice'}

a = {i for i in math if i not in en}
b = {j for j in en if j not in math}
c = {x for x in en if x in math}

print("數學及格英文不及格： ",a)
print("英文及格數學不及格： ",b)
print("兩者都及格： ",c)
print("總人數： ",len(a)+len(b)+len(c))