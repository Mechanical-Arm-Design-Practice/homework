class student:
    name = "NULL"
    gender = "gender"
    grades = []

    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

    def add(self,grade):
        self.grades.append(grade)

    def avg(self):
        temp = 0
        for loop in range(0,len(self.grades)):
            temp += self.grades[loop]
        avgg = temp /len(self.grades)
        return avgg

    def fcount(self):
        temp = 0
        for loop in range(0,len(self.grades)):
            if self.grades[loop] < 60:
                temp+=1
        
        return temp
    #def top(self):

while True:
    people = input("請輸入學生姓名")
    boygirl = input("請輸入學生性別")
    
    temp = student(people,boygirl)
    while True:
        score = int(input("請輸入成績"))
        temp.add(score)
        stop = input("是否要繼續輸入成績(y/n)")
        if stop == 'n':
            break

    alldata = {}
    alldata.setdefault(people,temp)
    allstop = input("是否要輸入其他學生(y/n)")
    if allstop == 'n':
        break

print(alldata[people].grades)

print(alldata[people].avg())
print("不及格的有",alldata[people].fcount())
