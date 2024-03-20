"""
学生接口层
"""
from DB import models


# 学生注册接口
def student_register_interface(student_name, student_pwd):
	# 判断学生是否已存在
	student_obj = models.Student.select(student_name)
	# 如果学生对象已存在，则返回视图层不允许在创建
	if student_obj:
		return False, f'{student_name} 学生用户已存在'
	else:
		# 如果学生不存在，则允许创建学生对象，调用学生类进行实例化创建，并保存
		student_obj = models.Student(student_name, student_pwd)
		# 调用save方法保存创建的对象
		student_obj.save()
		return True, f'{student_name} 学生创建成功'


# 学生登录接口

'''
def student_login_interface(student_name, student_pwd):
	# 调用学生类中的获取对象方法，获取对象，然后对获取的对象进行逻辑判断
	student_obj = models.Student.select(student_name)
	# 如果学生对象不存在
	if not student_obj:
		return False, f'{student_name}学生不存在，登录失败！'
	else:
		# 如果学生对象存在，则进行登录密码校验
		if student_pwd == student_obj.pwd:
			return True, f'{student_name} 学生登录成功！'
		else:
			return False, '密码错误'

'''


# 选择学校接口
def add_school_interface(school_name, student_name):
	# 先获取当前学生对象
	student_obj = models.Student.select(student_name)
	# 判断学生对象是否已选择了学校
	if student_obj.school:
		return False, '当前学生已选择过学校了！'
	# 若当前学生没有选择学校，则调用学生对象中的选择学校方法，实现学生添加学校
	student_obj.add_school(school_name)
	return True, f'{student_name} 已选择 {school_name} 学校成功!'


# 获取学生所在学校的所有课程
def get_course_list_interface(student_name):
	# 获取当前学生对象
	student_obj = models.Student.select(student_name)
	# 获取当前学生对应的学校名称
	school_name = student_obj.school
	# 判断当前学校名称是否为空,如为空则返回False
	if not school_name:
		return False, '没有学校,请先选择学校'
	# 如学校不为空,则获取当前学校对应可选的课程列表,先获取学校对象
	school_obj = models.School.select(school_name)
	# 判断当前学生对象是否有课程可选，若无，则需要联系管理员
	course_list = school_obj.course_list
	if not course_list:
		return False, '当前学校没有课程，请联系管理员创建课程！'
	# 如有，直接返回课程列表
	return True, course_list


# 学生选择课程接口
def add_course_interface(course_name, student_name):
	# 1、判断当前课程是否已经存在学生课程列表中
	student_obj = models.Student.select(student_name)
	if course_name in student_obj.course_list:
		return False, '该课程已经选择过了'
	else:
		# 调用学生对象中添加课程的方法
		student_obj.add_course(course_name)
		return True, f'{course_name}课程已经添加成功'


# 学生查看分数接口
def check_score_interface(student_name):
	student_obj = models.Student.select(student_name)
	if student_obj.score_dict:
		return student_obj.score_dict

















