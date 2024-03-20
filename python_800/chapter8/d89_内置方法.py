"""
1、什么是内置方法？
定义在类内部，以__开头并以__结尾的方法

2、内置方法特点
会在某种情况下自动触发执行

3、为何要使用内置方法
为了定制化 类 或 对象

4、如何使用内置方法？
以__str__和 __del__进行讲解：

__str__():在打印对象时会自动触发，然后将返回值(必须是字符串类型)  当作本次打印的结果输出
__del__():在清理对象时触发，会在清除对象之前，先执行该方法
"""


class People:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	@property
	def say(self):
		return f'<{self.name}  :  {self.age}>'

	def __str__(self):
		return f'{self.name} : {self.age}'

	def __del__(self):
		print('run.....')


p = People('王晓涵', 23)
# print(p.say)
# 打印p，实际上是在运行 p.__str__() 方法
print(p)
print('======================>')












