math = {'Tom','John','Mary','Jimmy','Summy','Amy'}
english ={'John','Mary','Tony','Bob','Pony','Tom','Alice'}
print("only math:",math-english)
print("only english:",english-math)
print("all pass:",math&english)
print("class size:",len(math|english))
print("====================================")
Tom_score=[80,100,90,95]
John_score=[100,93,75,80]
data= {"Tom":Tom_score,"John":John_score}
print("Tom's average score:",sum(data["Tom"])/len(data["Tom"]))
print("John's average score:",sum(data["John"])/len(data["John"]))