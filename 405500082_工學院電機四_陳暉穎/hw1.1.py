math = {'Tom', 'John', 'Mary', 'Jimmy', 'Sunny','Amy'}
english = {'John', 'Mary' , 'Tony' , 'Bob' , 'Pony', 'Tom' , 'Alice'}

print("math&english pass")
print(math&english)
print("only math pass")
print(math-english)
print("only english pass")
print(english-math)

classmate = len(math|english)

print(classmate)