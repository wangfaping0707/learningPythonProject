class Course:
	def __init__(self, name, period, price):
		self.name = name
		self.period = period
		self.price = price

	def tell_info(self):
		print(f'<课程名称：{self.name}  课程周期：{self.period}  课程价格：{self.price}>')


course_obj1 = Course('python全栈开发', '6mons', 20000)
course_obj2 = Course('Linux运维', '5mons', 18000)
course_obj3 = Course('自动化运维', '7mons', 28000)

