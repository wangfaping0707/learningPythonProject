from d77_people import *


class Student(People):
	def __init__(self, name, age, sex, stu_id):
		People.__init__(self, name, age, sex)
		self.stu_id = stu_id

	def choose_course(self):
		print(f'{self.name} 正在选课！！！')


s = Student('小鱼儿', 18, 'female', 2010109001)
s.choose_course()