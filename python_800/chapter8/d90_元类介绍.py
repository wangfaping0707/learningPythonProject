"""
# 什么是元类？
元类就是用来实例化产生类的类；
关系：元类---实例化--->类(People)---实例化---对象(obj)
"""


class People:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	@property
	def say(self):
		return f'<{self.name}  :  {self.age}>'


obj = People('egon', 18)
# 查看内置的元类：我们用class关键字定义所有的类，以及内置的类 都是由内置的元类 type 帮我们实例化产生
print('查看元类：', type(People))
