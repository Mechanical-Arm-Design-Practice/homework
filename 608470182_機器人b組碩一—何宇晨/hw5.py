class Student:

    def __init__(self, n, g):
        self.name = n
        self.gender = g
        self.grades = []

    def add(self,grade):
        self.grades.append(grade)

    def avg(self):
        avg_grade = sum(self.grades)/len(self.grades)
        return avg_grade

    def fcount(self):
        fail_count = 0
        for i in self.grades:
            if i < 60:
                fail_count += 1
        return fail_count
    
    def __str__(self):
        return "Name:%s Avg:%.2f 不及個:%d" % (self.name, self.avg(), self.fcount())
    
    @classmethod
    def top(cls, *students):
        tops = students[0]
        for s in students:
            print(s.grades)
        return tops
    
s1 = Student("Tom","M")
s2 = Student("Jane","F")
s3 = Student("John","M")
s4 = Student("Ann","F")
s5 = Student("Peter","M")
s1.add(80)
s1.add(90)
s1.add(55)
s1.add(77)
s1.add(40)
s2.add(58)
s2.add(87)
s3.add(100)
s3.add(80)
s4.add(40)
s4.add(55)
s5.add(60)
s5.add(60)

print(str(s1))
print(str(s2))
print(str(s3))
print(str(s4))
print(str(s5))
tops = Student.top(s1,s2,s3,s4,s5)
print("最高分的同學:{} 平均分數:{}".format(tops.name, tops.avg()))