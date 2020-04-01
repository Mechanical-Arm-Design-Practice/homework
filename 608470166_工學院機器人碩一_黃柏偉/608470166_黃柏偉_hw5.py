class Student:
	def __init__(self,name,gender):
		self.name=name
		self.gender=gender
		self.grades=[]
	def avg(self):
		return sum(self.grades)/len(self.grades)
	def add(self,grade):
		self.grades.append(grade)
	def fcount(self):
		count=0
		for grade in self.grades:
			if grade<60:
				count+=1
		return count
	def top(self,all):
		a=[]
		for n in all:
			a.append(n.avg())
		
		return all[a.index(max(a))].name
	
		




def main():
	all=[]
	while 1:
		x=input("是否新增學生(y/n)")
		if x=="y":
			person = Student(input("請輸入姓名"),input("請輸入性別(m/f)"))
			person.add(int(input("請輸入成績")))
			while 1:
				y=input("是否繼續輸入成績(y/n)")
				if y=="y":
					person.add(int(input("請輸入成績")))
				else:
					all.append(person)
					break
		else:
			break
	for n in all:
		print("學生",n.name,"平均成績:",n.avg(),"不及格數目:",n.fcount())
	print("平均分數最高的學生:",person.top(all))
	


		

	


if __name__ == "__main__":
    main()