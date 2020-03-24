math,english = {'Tom','John','Mary','Jimmy','Sunny','Amy'},{'John','Mary','Tony','Bob','Pony','Tom','Alice'}
print(math - english,"math is pass")
print(english - math,"english is pass")
print(english & math,"all pass")
print(len(english | math),"student")

data = {"Tom":[80,100,90,95],"John":[100,93,75,80]}
print("Tom's grade is",sum(data["Tom"])/len(data["Tom"]))
print("John's grade is",sum(data["John"])/len(data["John"]))

