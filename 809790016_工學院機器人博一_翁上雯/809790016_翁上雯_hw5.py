class Student:

    count=0
    members={}

    def __init__(self, name, gender, grades):
        self.name = name
        self.gender = gender
        self.grades = grades
        Student.count+=1
        Student.members[name]=[gender, grades]
 
    def avg(self):
        cnt = len(self.grades)
        score_sum = sum(self.grades[0:cnt])
        self.average=score_sum/float(cnt)
        return self.average

    def add(self, grade):
        self.grades.append(grade)

    def fcount(self):
        fail_cnt=0
        for i in self.grades:
            if(i<60):
                fail_cnt=fail_cnt+1
        return fail_cnt

    def print_grades(self):
        print(self.grades)

    def exclame(self):
        width1=8
        width2=20
        print(self.name.center(width1), ":",('%s'%self.grades).ljust(width2), "=> Avg =",'%.3f'%self.avg(), ", Failed # =", self.fcount())

   
    #@classmethod 
    def top(*person):
        highest_avg_score=0.0
        hightest_avg_student=[]
        for n in person:
            if(n.avg()>highest_avg_score):
                highest_avg_score=n.avg()
                hightest_avg_student=[]
                hightest_avg_student=n.name
            elif(n.avg()==highest_avg_score):
                hightest_avg_student.append(n.name)
        print(hightest_avg_student," has highest score ", highest_avg_score," in class.")

def main():

    s1 = Student("Jenny","Female",[82,58])
    s2 = Student("Jonah","Male",[100,88])
    s3 = Student("Aaron","Male",[30,45])

    print("\n====Q1====")
    print("Add grade to grade list:")
    s1.add(99)
    s2.add(95)
    s3.add(95)
    print("done!")

    print("\n====Q2====")
    print("Print out (1) average score & (2) number of subjects failed:")
    s1.exclame()
    s2.exclame()
    s3.exclame()

    print("\n====Q3====")
    Student.top(s1,s2,s3)

if __name__ == "__main__":
    main()