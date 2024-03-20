"""
公告接口方法
"""
import os
from CONF import settings
from DB import models


# 获取所有学校名称接口
def get_all_school_interface():
	# 获取学校文件夹路径
	school_dir = os.path.join(settings.DB_PATH, 'School')
	# 判断文件夹是否存在
	if not os.path.exists(school_dir):
		return False, '没有学校，请先联系管理员！'
	# 文件夹若存在，则获取文件夹下面所有文件
	school_list = os.listdir(school_dir)
	return True, school_list


# 公共登录接口
def login_interface(user, pwd, user_type):
	if user_type == 'admin':
		obj = models.Admin.select(user)
	elif user_type == 'student':
		obj = models.Student.select(user)
	elif user_type == 'teacher':
		obj = models.Teacher.select(user)
	else:
		return False, '登录角色不对，请重新输入！'
	# 对获取到的角色进行判定
	# 如果角色存在
	if obj:
		# 若用户存在，则进行登录密码校验
		if pwd == obj.pwd:
			return True, f'{user} 登录成功'
		else:
			return False, '密码错误！'
	else:
		return False, '当前登录用户不存在！！！'


# 获取学校下所有课程接口
def get_course_in_school_interface(school_name):
	# 获取学校对象
	school_obj = models.School.select(school_name)
	# 获取学校对象下的所有课程
	course_list = school_obj.course_list
	# 对获取的课程进行为空判断
	if not course_list:
		return False, f'{school_name} 学校还没有课程！'
	return True, course_list


















