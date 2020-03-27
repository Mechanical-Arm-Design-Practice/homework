print("=====================    Q1  =======================================")
english_pass = {'Tom', 'John', 'Mary', 'Jimmy', 'Sunny', 'Amy'}
math_pass = {'John', 'Mary' , 'Tony' , 'Bob' , 'Pony', 'Tom' , 'Alice'}

print("只有英文及格: ")
for i in english_pass :
    if i not in math_pass:
        print(i)
print("")

print("只有數學及格: ")
for i in math_pass :
    if i not in english_pass:
        print(i)
print("")

print("兩科都及格: ")
for i in english_pass :
    if i in math_pass:
        print(i)
print("")

student = english_pass | math_pass
print("全班共有",len(student),"位同學")
print("")

print("=====================    Q2  =======================================")

list1 = [80,100,90,95]
list2 = [100,93,75,80]
dict1 = {"Tom":list1,"John":list2}
print(dict1)

score = 0
for i in range (len(list1)):
    score += list1[i]
print("Ton 的平均分數為: ",score/len(list1))

score = 0
for i in range (len(list2)):
    score += list2[i]
print("John 的平均分數為: ",score/len(list2))

