'''
多继承的正确打开方式：mixins机制
1、mixins机制核心：就是在多继承背景下尽可能的提升多继承的可读性
2、让多继承满足人的思维习惯=》什么是什么
'''


class Vehicle:
	pass


class FlyableMixin:
	def fly(self):
		print('具有飞行功能哦')


# 民航飞机
class CivilAircraft(FlyableMixin, Vehicle):
	pass


# 直升飞机
class Helicopter(FlyableMixin, Vehicle):
	pass


# 汽车
class Car(Vehicle):
	pass
