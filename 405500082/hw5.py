class Student():
    
    
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
        self.grades = []

    
    def avg(self):
        sum=0
        avg=0
        for i in range(len(self.grades)):
            self.grade=int(self.grades[i])
            sum=sum+self.grade
        
        avg=sum/len(self.grades)
        return avg
    

    def add(self,new_grades):
        self.grades.append(new_grades)

    
    def fcount(self):
        count=0
        for i in range(len(self.grades)):
            self.grade=int(self.grades[i])
            if (self.grade < 60):
                count+=1
        return count

    
    def print_data(self):
        print(self.name,self.gender)
        print("the aveage=",self.avg())
        print("the fail=",self.fcount())
    

def top(*studet_data):
        top_avg=0
        first = 0
        for i in range(len(studet_data)):
            student_avg=studet_data[i].avg()
            if student_avg > top_avg:
                top_avg=student_avg
                first=i
        print("the top is",studet_data[first].name)


Student1=Student('kirito',"male")
Student1.add(48)
Student1.add(76)
Student1.add(3)
Student1.print_data()


Student2=Student('banana',"male")
Student2.add(70)
Student2.add(65)
Student2.add(63)
Student2.print_data()


Student3=Student('van',"male")
Student3.add(12)
Student3.add(13)
Student3.add(14)
Student3.print_data()


top(Student1,Student2,Student3)



    





