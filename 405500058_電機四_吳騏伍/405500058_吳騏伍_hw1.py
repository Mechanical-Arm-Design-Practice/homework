print('###result###')
math={'Tom','John','Mary','Jimmy','Sunny','Amy'}
english={'John','Mary','Tony','Bob','Pony','Tom','Alice'}
s=math|english
math_only=math-english
english_only=english-math
print('math pass only >>',math_only)
print('english pass only >>',english_only)
print('This class has',len(s),'students.')
print('')

print('-----dict-----')
score={'Tom':[80,100,90,95],'John':[100,93,75,80]}
Tom_total=0
John_total=0
for i in range(4):
    Tom_total+=score['Tom'][i]
    John_total+=score['John'][i]
Tom_avg=Tom_total/4
John_avg=John_total/4
print("Tom's average score is",Tom_avg)
print("John's average score is",John_avg)
print('')

print('-----list-----')
Tom_score=[80,100,90,95]
John_score=[100,93,75,80]
Tom_total=0
John_total=0
for i in range(4):
    Tom_total+=Tom_score[i]
    John_total+=John_score[i]
Tom_avg=Tom_total/4
John_avg=John_total/4
print("Tom's average score is",Tom_avg)
print("John's average score is",John_avg)