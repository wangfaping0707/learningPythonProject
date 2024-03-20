'''
1、装饰器是在不修改 被装饰对象源代码以及调用方式的前提下为被装饰对象添加新功能的可调用对象；
2、装饰器是可调用对象，可调用对象有函数、类；
3、property是一个类,所以property也可以当成装饰器来用
4、property是一个装饰器，是用来将对象的一个方法伪造成 对象的一个属性
'''


class People:
	def __init__(self, name, weight, height):
		self.name = name
		self.weight = weight
		self.height = height

	@property
	def bmi(self):
		return self.weight / (self.height ** 2)


p1 = People('夏鸥', 69, 1.69)
# print(p1.bmi())
print(p1.bmi)
