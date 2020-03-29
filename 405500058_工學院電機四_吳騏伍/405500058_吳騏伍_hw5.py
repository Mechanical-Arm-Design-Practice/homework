print('\n###result###')
class Student:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
        self.grades=[]

    def add(self,added_new_grade):
        self.grades.append(added_new_grade)

    def avg(self):
        total=0
        if(len(self.grades) > 0):
            for i in range(0,len(self.grades)):
                total+=self.grades[i]
            return total/len(self.grades)

    def fcount(self):
        fail_cnt=0
        for i in range(0,len(self.grades)):
            if(self.grades[i] < 60):
                fail_cnt+=1
        return fail_cnt

    def Output(self):
        print("Name:%s"%(self.name),"\t","gender:%s"%(self.gender),"\t","grades:%d"%(self.avg()),"\t","不及格 %d"%(self.fcount()),"次")

def top(*Student):
    score_list=[]
    for i in range(0,len(Student)):
        score_list.append(Student[i].avg())
    score_list.sort()
    for i in range(0,len(Student)):
        if( (score_list[len(Student)-1]) == Student[i].avg() ):
            print("平均分數最高的學生是%s"%Student[i].name)

def main():
    person_1=Student("Grace","female")
    person_1.add(50)
    person_1.add(70)
    person_1.Output()

    person_2=Student("Jack","male")
    person_2.add(40)
    person_2.add(50)
    person_2.Output()

    person_3=Student("Steve","male")
    person_3.add(100)
    person_3.add(100)
    person_3.Output()

    top(person_1,person_2,person_3)

if __name__ == "__main__":
    main()