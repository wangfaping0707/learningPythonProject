"""
用于存放类的：
学校类、学员类、课程类、讲师类、管理员类
"""
from DB import db_handler


# 父类，让所有字类都继承save select方法
class Base:
	def save(self):
		# 让db_handler中的save_data帮我保存数据
		db_handler.save_data(self)

	# 获取数据
	@classmethod
	def select(cls, username):
		# obj :对象 or None
		obj = db_handler.select_data(cls, username)
		return obj


# 管理员类
class Admin(Base):
	# 调用类的时候触发
	def __init__(self, username, pwd):
		self.name = username
		self.pwd = pwd

	# # 保存数据->注册、保存、更新数据
	# def save(self):
	# 	# 让db_handler中的save_data帮我保存数据
	# 	db_handler.save_data(self)
	#
	# # 获取数据
	# @classmethod
	# def select(cls, username):
	# 	# obj :对象 or None
	# 	obj = db_handler.select_data(cls, username)
	# 	return obj

	# 创建学校
	def create_school(self, school_name, school_addr):
		# 该方法来调用学校类，并实例化对象保存
		school_obj = School(school_name, school_addr)
		school_obj.save()

	# 创建课程
	def create_course(self, school_obj, course_name):
		# 调用课程类,实例化创建课程
		course_obj = Course(course_name)
		# 保存创建的课程对象
		course_obj.save()
		# 获取学校对象，并将当前创建的课程添加进去
		school_obj.course_list.append(course_name)
		# 更新学校数据
		school_obj.save()

	# 创建讲师
	def create_teacher(self, teacher_name, teacher_pwd):
		# 调用老师类，来实例化创建老师对象
		teacher_obj = Teacher(teacher_name, teacher_pwd)
		teacher_obj.save()


# 学校类
class School(Base):
	def __init__(self, school_name, school_addr):
		# 必须写：self.user因为db_handler里面的select_data统一规范
		self.name = school_name
		self.school_addr = school_addr
		# 课程列表：每所学校都应该有响应的课程
		self.course_list = []


# # 保存数据->注册、保存、更新数据
# def save(self):
# 	# 让db_handler中的save_data帮我保存数据
# 	db_handler.save_data(self)
#
# # 获取数据
# @classmethod
# def select(cls, username):
# 	# obj :对象 or None
# 	obj = db_handler.select_data(cls, username)
# 	return obj


class Student(Base):
	def __init__(self, student_name, student_pwd):
		self.name = student_name
		self.pwd = student_pwd
		# 每个学生只能有一个校区
		self.school = None
		# 一个学生可以选择多门课程
		self.course_list = []
		# 学生课程分数
		self.score_dict = {}

	# 学生添加学校方法
	def add_school(self, school_name):
		self.school = school_name
		self.save()

	# 学生添加课程方法
	def add_course(self, course_name):
		# 1、学生课程列表添加课程
		self.course_list.append(course_name)
		self.save()

		# 2、给学生选择的课程设置默认分数
		self.score_dict[course_name] = 0
		self.save()

		# 3、学生选择的课程对象，添加对应的学生
		course_obj = Course.select(course_name)
		course_obj.student_list.append(
			self.name
		)
		course_obj.save()


class Course(Base):
	def __init__(self, course_name):
		self.name = course_name
		self.student_list = []


class Teacher(Base):
	def __init__(self, teacher_name, teacher_pwd):
		self.name = teacher_name
		self.pwd = teacher_pwd
		self.course_list_from_tea = []

	# 老师添加课程方法
	def add_course(self, course_name):
		self.course_list_from_tea.append(course_name)
		self.save()

	# 老师查看教授课程方法
	def show_course(self):
		return self.course_list_from_tea

	# 老师获取课程下的学生方法
	def get_student(self, course_name):
		# 获取课程对象
		course_obj = Course.select(course_name)
		return course_obj.student_list

	# 老师修改学生分数方法
	def change_score(self, course_name, student_name, score):
		# 1.获取学生对象
		student_obj = Student.select(student_name)
		# 2.在给学生对象中的课程修改分数
		student_obj.score_dict[course_name] = score
		student_obj.save()




