from d74_课程类 import *


class Class:
	def __init__(self, name):
		self.name = name
		self.course = None

	def related_course(self, course_obj):
		self.course = course_obj

	def tell_course(self):
		print(f'班级名：{self.name}')
		self.course.tell_info()  # 打印课程的详细信息


class_c1 = Class('脱产14期')
class_c2 = Class('脱产15期')
class_c3 = Class('脱产29期')
# 为班级关联课程对象
class_c1.related_course(course_obj1)
class_c2.related_course(course_obj2)
class_c3.related_course(course_obj3)

if __name__ == '__main__':
	class_c1.tell_course()
	class_c2.tell_course()
	class_c3.tell_course()
