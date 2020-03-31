class Student():
    def  __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.grades = []
        
    def avg (self):
        sum = 0
        for i in range(len(self.grades)):
            self.grade = int(self.grades[i])
            sum += self.grade
        average = sum/len(self.grades)
        return average
    def add(self,score):
        self.grades.append(score)

    def fcount(self):
        fcnt = 0
        for i in range(len(self.grades)):
            if self.grades[i] < 60:
                fcnt += 1
        print("fail subjects:%d" %fcnt)

    def alldata(self):
        print("name:",self.name,"gender:",self.gender)
        print("avg:",self.avg(),",fail:",self.fcount())

def top(*person):
    top_score = -1
    index = 0
    for i in range(len(person)):
        avg_person = person[i].avg()
        if avg_person > top_score:
            top_score = avg_person
            index = i
    if index:
        print(person[index].name,"got highest score.") 

Student1 = Student('A','male')
Student1.add(20)
Student1.add(30)
Student1.add(40)
Student1.add(50)
Student1.alldata()
print("\n")
Student2 = Student('B','male')
Student2.add(50)
Student2.add(60)
Student2.add(70)
Student2.add(80)
Student2.alldata()
print("\n")
Student3 = Student('C','female')
Student3.add(60)
Student3.add(60)
Student3.add(60)
Student3.add(60)
Student3.alldata()
print("\n")
top(Student1,Student2,Student3)