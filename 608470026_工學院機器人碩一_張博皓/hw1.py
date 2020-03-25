print('\n*****************hw1-1 begin*****************\n')

math = {'Tom','John','Mary','Jimmy','Sunny','Amy'}
english = {'John','Mary','Tony','Bob','Pony','Tom','Alice'}

print(math & english , 'all pass')
print(math-(math & english) , 'math pass but english never pass')
print(english-(math & english) , 'math pass but english never pass')

print('\n*****************hw1-2 begin*****************\n')


score = {'Tom':[80,100,90,95],'John':[100,93,75,80]}

print("Tom's averange is",((score['Tom'][0]+score['Tom'][1]+score['Tom'][2]+score['Tom'][3])/4))

print("John's averange is",((score['John'][0]+score['John'][1]+score['John'][2]+score['John'][3])/4))
