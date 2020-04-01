class student:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.grades = []
    
    def avg(self):
        sum = 0
        for i in range(len(self.grades)):
            sum += self.grades[i]
        return sum/len(self.grades)

    def add(self, add_grade):
        self.grades.append(add_grade)

    def fcount(self):
        cnt = 0
        for i in range(len(self.grades)):
            if self.grades[i] < 60:
                cnt += 1
        return cnt

    def output(self):
        print(self.name, '不及格總數:%d'%(self.fcount()), '平均分數：%f'%(self.avg()))
        


student1 = student('Lin', 'm')
student1.add(80)
student1.add(70)
student1.add(50)
student1.output()

student2 = student('Wang', 'm')
student2.add(25)
student2.add(48)
student2.add(69)
student2.output()

student3 = student('Chen', 'm')
student3.add(54)
student3.add(81)
student3.add(70)
student3.output()

