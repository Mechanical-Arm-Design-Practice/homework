class Student:
	def __init__(self, name, gender):
		self.name = name
		self.gender = gender
		self.grades = []


	def avg(self):
		average = sum(self.grades)/len(self.grades)		
		return(average)


	def add(self,grade):
		self.grades.append(grade)
	

	def fcount(self):
		x=0
		for n in self.grades:
			if n < 60:
				x+=1
		return(x)
	

	def top(self,classroom):
		top_grade = 0
		for people in classroom:
			if people.avg() > top_grade:	 
				top_grade = people.avg()
				top_student = people.name
		return (top_grade,top_student)


if __name__ == "__main__":
	classroom = []
	student_num = 1
	while(1) :
		print("學生 %d : "% student_num,end =' ')
		name = input()
		gender = input("性別(b/g) : ")
		student = Student(name,gender)
		classroom.append(student)
		if  input("還有學生？(y/n): ") != "y" :
			break
		student_num = student_num + 1
	for people in classroom:
		print("學生 ",people.name," 成績 : ",end=' ')
		grades = input()
		all_grades = list(map(int, grades.split()))
		for n in range(len(all_grades)) :
			people.add(all_grades[n])
		print("學生：",people.name,"平均為 ",people.avg(),"不及格數目為",people.fcount())
	top_grade,top_student = student.top(classroom)
	print("最高平均是:",top_student,"   分數為：",top_grade)
	
