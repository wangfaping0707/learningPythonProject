class Student:
	# 定义对象的初始化方法
	def __init__(self, name, age, gender):
		self.name = name
		self.age = age
		self.gender = gender

	str = '这是对象的共有变量'

	def tell_info(self):
		print(123)


stu = Student('egon', 18, 'male')
print(stu.__dict__)
print(Student.__dict__)

'''
总结__init__方法：
1、会在调用类创建空对象之后，自动触发执行，用来为对象初始化自己独有的数据
2、__init__应该存放的是为对象初始化属性的功能，但是也可以存放其他任意代码，想要在类调用时就立刻执行的代码都可以放到该方法内；
3、__init__必须返回None

'''