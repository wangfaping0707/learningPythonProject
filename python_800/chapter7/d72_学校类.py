# import d73_班级类
# import d73_班级类
from d73_班级类 import *


# import os
# print(__file__)
# print(os.path.dirname(__file__))
class School:
	# 定义一个校区类，每个小区都是不一样，所以需要初始化对应小区
	school_name = '老男孩校区'

	def __init__(self, nick_name, addr):
		self.nick_name = nick_name
		self.addr = addr
		self.classes = []

	# 为小区添加班级，并保存
	def related_class(self, class_obj):
		self.classes.append(class_obj)

	# 查询某个校区下面有多少班级
	def tell_class(self):
		print(f'当前校区是:{self.nick_name}')
		for class_obj in self.classes:
			class_obj.tell_course()


s1 = School('老男孩上海校区', '浦东新区')
s2 = School('老男孩深圳校区', '南山区')
s1.related_class(class_c1)
s1.related_class(class_c2)
s2.related_class(class_c3)

s1.tell_class()
print('----------------------------------------------------------')
s2.tell_class()
