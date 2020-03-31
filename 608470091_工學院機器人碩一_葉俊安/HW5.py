class Student():

    def __init__(self,n,g):
        self.name = n
        self.gender = g
        self.grades = []


    def add(self,grades):
        self.grades.append(grades)
    
    def avg(self,):
        n = sum(self.grades)/len(self.grades)
        return n

    def fcount(self):
        x = 0
        for i in self.grades:
            if i < 60:
                x+=1
        return x
    
    def top(*Student):
        topg = 0
        tops = ''
        for i in Student:
            if i.avg() > topg:
                topg = i.avg()
                tops = i.name
        return tops


def main():
    
    s1 = Student("a","M")
    s2 = Student("b","F")
    s3 = Student("c","M")

    s1.add(80)
    s1.add(60)
    s1.add(55)
    s2.add(95)
    s2.add(65)
    s2.add(80)
    s3.add(87)
    s3.add(93)
    s3.add(45)

    s = [s1,s2,s3]

    print("\n")
    print(s1.name,s1.gender,s1.grades,'平均值：',s1.avg(),'不及格總數：',s1.fcount())
    print(s2.name,s2.gender,s2.grades,'平均值：',s2.avg(),'不及格總數：',s2.fcount())
    print(s3.name,s3.gender,s3.grades,'平均值：',s3.avg(),'不及格總數：',s3.fcount())
    print('平均最高分的同學：',Student.top(*s))

if __name__ == "__main__":
    main()