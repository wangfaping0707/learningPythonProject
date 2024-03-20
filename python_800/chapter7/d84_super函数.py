'''
调用super()函数，会产生一个特殊的对象，该对象专门用来引用父类的属性，且严格按照MRO规定的顺序向后查找
该对象会参照属性查找发起类的MRO，去当前类的父类中查找
提示：在python2中，super的使用需要完整的写成super(自己的类名，self)，而在python3中可以简写成super()
'''


class People:
	def __init__(self, name, age, sex):
		self.name = name
		self.age = age
		self.sex = sex


class Teacher(People):
	def __init__(self, name, age, sex, salary, level):
		super().__init__(name, age, sex)
		self.salary = salary
		self.level = level


obj_t = Teacher('egon', 29, 'male', 99000, 10)
print(obj_t.name)
