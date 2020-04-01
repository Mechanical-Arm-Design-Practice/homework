import math

print('\n---------1---------\n')

print('登幽州臺歌\t陳子昂\n前不見古人\t後不見來者\n念天地之悠悠\t獨愴然而涕下')


print('\n---------2---------\n')

a = 3
b = 4
c = 5 #a, b, c = 3, 4, 5
p = (a+b+c)/2
s = math.sqrt(p*(p-a)*(p-b)*(p-c)) #(p*(p-a)*(p-b)*(p-c))**0.5
print(s)


print('\n---------3---------\n')

str = 'PLEASE CONVERT THIS SENTENCE TO LOWER CASE.'
print(str.lower())


print('\n---------4---------\n')

bornYear = int(input("請輸入你的出生年份："))
nowYear = int(input("請輸入今年的年份："))
age = nowYear - bornYear
print("你今年%d歲" % age)


print('\n---------5---------\n')

year = int(input("請輸入西元年份："))

if((year%4 == 0 and year%100 != 0)or(year%400 == 0)):
    print('閏年')
else:
    print('平年')


print('\n---------6---------\n')

ans = int(input('請輸入答對題數：'))
first_points = ans//8
if(first_points == 1):
    second_points = ans%8
    total = 64 + second_points*6
else:
    total = ans*8
print(total, '分')


print('\n---------7---------\n')

# list_1 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# for i in list_1:
#     print(i)
#     for j in list_1:
#         print(j)
#         if(list_1[i]>list_1[i+1]):
#             list_1[i], list_1[i+1] = list_1[i+1], list_1[i]
#             print(list_1[i+1], list_1[i])
# print(list_1)


print('\n---------8---------\n')

list2_3 = [[1, 2, 3], [4, 5, 6]]
print(list2_3[1][2])