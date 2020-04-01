class student:
    name = "NULL"
    gender = "gender"
    grades = []

    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
        self.grades = []

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
    def top(self,alldata):  
        avgmax = 0
        for loop in alldata.keys():
            if alldata[loop].avg() > avgmax:
                avgmax = alldata[loop].avg()
                superstudent = loop
        return superstudent


alldata = {}
while True:
    people = input("請輸入學生姓名")
    boygirl = input("請輸入學生性別")
    
    temp = student(people,boygirl)
    while True:
        score = int(input("請輸入成績"))
        temp.add(score)
        ynflag = True;
        while ynflag:
            stop = input("是否要繼續輸入成績(y/n)")
            if stop == 'y' or stop == 'n':
                ynflag = False
            else:
                ynflag = True
        if stop == 'n':
            break

    alldata.setdefault(people,temp)
    ynflag = True
    while ynflag:
        allstop = input("是否要輸入其他學生(y/n)")
        if allstop == 'y' or allstop == 'n':
            ynflag = False
        else:
            ynflag = True
    if allstop == 'n':
        break

for loop in alldata.keys():
    print(alldata[loop].name,"的成績平均為",alldata[loop].avg(),",不及格的有",alldata[loop].fcount(),"科")

print("平均最高的為",temp.top(alldata))

