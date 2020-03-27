class Student():

    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
        self.grades = []
        
    def avg(self):
        averge = 0
        for i in range (len(self.grades)):
            self.grade = int(self.grades[i])
            averge =  averge + self.grade

        averge = averge/len(self.grades)
        return averge

    def add(self,element):
        self.grades.append(element)

    def fcount(self):
        cnt = 0
        for i in range (len(self.grades)):
            if self.grades[i] < 60:
                cnt = cnt +1
        return cnt

    def print_std(self):
        print(self.name,", ",self.gender)
        print(self.avg())
        print(self.fcount())

def top(*stud):
    top_avg = -1
    index = -1

    for i in range (len(stud)):
        avg_stud = stud[i].avg()
        if avg_stud > top_avg:
            top_avg = avg_stud
            index = i
    
    if index != -1:
        print(stud[index].name," is the top student !!!")


Student1 = Student('John',"male")
Student1.add(54)
Student1.add(70)
Student1.add(59)
Student1.print_std()
print("==========================================")
Student2 = Student('Any','female')
Student2.add(63)
Student2.add(51)
Student2.add(68)
Student2.print_std()
print("==========================================")
Student3 = Student('Khon',"male")
Student3.add(54)
Student3.add(59)
Student3.add(53)
Student3.print_std()
print("==========================================")
top(Student1,Student2,Student3)

