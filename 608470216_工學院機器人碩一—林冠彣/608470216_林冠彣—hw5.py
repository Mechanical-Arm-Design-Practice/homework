class Student():
    
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.grades = []
    

    def avg(self):
        
        Avg = sum(self.grades)/len(self.grades)
        return Avg


    def add(self,grade):

        self.grades.append(grade)


    def fcount(self):
        count = 0
        for i in range(len(self.grades)):
            if self.grades[i] < 60:
                count = count + 1
        return count


    def top(self,Students):
        highscore = 0
        for i in Students:
            tmp = i.avg()
            if highscore < tmp :
                highscore =  tmp
                people = i.name

        return highscore,people

if __name__ == "__main__":

    Students = []
    classmate = 0
    allgrades = list()
    while 1 :
        Name = input("Please enter student's name : ")
        Gender = input ("Please enter student's gender : ")
        temp = Student(Name,Gender)
        while 1:
            Grades = int(input ("Please enter student's grades : "))
            NextGrades = input ("Do you need to enter the next Grades?(Y/N)")
            temp.add(Grades)
            if NextGrades == 'N':
                break
            else :
                continue            
        Students.append(temp)
        print("Name = ",Students[classmate].name,"avg = ",Students[classmate].avg(),"fail = ",Students[classmate].fcount())
        Next = input ("Do you need to enter the next student?(Y/N)")
        if Next == 'N':           
            highscore,people = temp.top(Students)
            print("平均分數最高 ： " ,people,"分數 ： ",highscore)
            break
        else :
            classmate = classmate + 1
            continue