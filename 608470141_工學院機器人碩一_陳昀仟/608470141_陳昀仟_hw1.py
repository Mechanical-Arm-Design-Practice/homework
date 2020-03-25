# Q1. 使用set型別完成下列問題: 本班期末考試
#  數學及格的有: Tom, John, Mary, Jimmy, Sunny, Amy
#  英文及格的有: John, Mary , Tony , Bob , Pony, Tom , Alice
#  分別印出數學及格但英文不及格的名單,數學不及格但英文及格的名
# 單,兩科都及格的名單
#  最後印出全班總共有幾個同學

# Q2. 使用dict,list 型別完成下列問題:
#  Tom 作業成績為80, 100, 90, 95,John 作業成績為100,93,75,80
#  請以dict 型別存放兩個同學的資料key:名字,value:分數列表(list)
#  請分別算出兩位同學的平均分數並且印出

math = {"Tom", "John", "Mary", "Jimmy", "Sunny", "Amy"}
english = {"John", "Mary", "Tony", "Bob", "Pony", "Tom", "Alice"}

print("數學及格英文不及格", math - english)
print("英文及格數學不及格", english - math)
print("兩科及格", math & english)

Grade = {
    "Tom": [80, 100, 90, 95],
    "John": [100, 93, 75, 80]
}


def list_average(x):
    sum = 0
    for i in x:
        sum += i
    sum /= len(x)
    return sum


print("Tom 平均成績：", list_average(Grade.get("Tom")))
print("John 平均成績：", list_average(Grade.get("John")))
