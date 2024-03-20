"""
老师接口层
"""
from DB import models
from INTERFACE import common_interface


# 老师查看课程接口
def check_course_interface(teacher_name):
	# 获取当前老师对象
	teacher_obj = models.Teacher.select(teacher_name)

	# 让老师对象调用查看课程方法，并返回课程
	course_list = teacher_obj.show_course()
	# 对返回课程列表值进行校验
	if not course_list:
		return False, f'{teacher_name} 老师还没选择课程！'
	else:
		return True, course_list


# 老师添加课程接口
def add_course_interface(course_name, teacher_name):
	# 获取当前老师对象
	teacher_obj = models.Teacher.select(teacher_name)
	# 判断当前课程是否已存在老师课程列表中
	course_list = teacher_obj.course_list_from_tea
	# 已存在
	if course_name in course_list:
		return False, '该课程已存在！'
	# 不存在，则将课程添加到老师课程列表中
	teacher_obj.add_course(course_name)
	return True, '课程添加成功！！！'


# 老师获取课程下学生接口
def get_student_interface(course_name, teacher_name):
	# 获取当前老师类对象
	teacher_obj = models.Teacher.select(teacher_name)
	# 让当前老师对象，调用获取课程下所有学生功能
	student_list = teacher_obj.get_student(course_name)

	# 判断课程列表下是否有学生
	if not student_list:
		print('暂时没有学生选择该课程!!!')
	return True, student_list


# 老师修改分数接口
def change_score_interface(course_name, student_name, score, teacher_name):
	# 获取老师对象
	teacher_obj = models.Teacher.select(teacher_name)
	# 让老师对象调用修改分数方法
	teacher_obj.change_score(course_name, student_name, score)
	return True, '修改分数成功!'
