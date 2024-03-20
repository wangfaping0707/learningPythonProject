from d77_people import *


class Teacher(People):
	def __init__(self, name, age, sex, salary, level):
		People.__init__(self, name, age, sex)
		self.salary = salary
		self.level = level

	def score(self):
		print(f'老师 {self.name} 正在给学生打分！！！')


t = Teacher('egon', 31, 'male', 90000, 10)
t.score()
