print('hw1 Q1')
Math = {'Tom', 'John', 'Mary', 'Jimmy', 'Sunny', 'Amy'}
Eng = {'John', 'Mary' , 'Tony' , 'Bob' , 'Pony', 'Tom' , 'Alice'}
print((Math|Eng) - Eng, 'pass Math only')
print((Math|Eng) - Math, 'pass English only')
print(Math & Eng,'both pass')

print('hw1 Q2')
d1 = {"Tom":[80,100,90,95],"John":[100,93,75,80]}
print("Tom",sum(d1['Tom'])/4)
print("John",sum(d1['John'])/4)