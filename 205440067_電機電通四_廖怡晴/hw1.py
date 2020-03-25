print('\n---Q1---\n')
math = set(['Tom', 'John', 'Mary', 'Jimmy', 'Sunny', 'Amy'])
english = set(['John', 'Mary' , 'Tony' , 'Bob' , 'Pony', 'Tom' , 'Alice'])

print math - english
print english - math
print english & math
print(len(english|math))

print('\n---Q2---\n')

Tom_score = [80, 100, 90, 95]
John_score = [100, 93, 75, 80]
score = {'Tom': Tom_score, 'John': John_score}
ave_score = {'Tom': sum(Tom_score)/len(Tom_score), 'John': sum(John_score)/len(John_score)}
print ave_score