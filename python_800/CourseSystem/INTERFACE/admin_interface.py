"""
管理员注册接口
"""
from DB import models


# 管理员注册接口
def admin_register_interface(username, pwd):
	# 接收用户视图层传入的用户名和密码
	# 1、判断用户是否存在:调用Admin类中select方法，由该方法去调用db_handler中的select_data功能获取对象
	# admin_obj = models.Admin(username, pwd)
	# 2、若存在不允许注册，返回用户已存在给视图层
	admin_obj = models.Admin.select(username)
	if admin_obj:
		return False, '用户已存在'
	# 3、若不存在则允许注册，调用类实例化得到对象并保存
	admin_obj = models.Admin(username, pwd)
	# 	对象调用save()方法，会将admin_obj传给save
	admin_obj.save()
	return True, '用户注册成功'


# 管理员登录接口
def admin_login_interface(username, password):
	# 1、判断用户是否存在
	admin_obj = models.Admin.select(username)

	# 2、若不存在，则证明用户不存在并返还给视图层
	if not admin_obj:
		return False, '用户名不存在'

	# 3、若存在，则校验密码
	if password == admin_obj.pwd:
		return True, '登录成功'
	else:
		return False, '密码错误'


# 管理员创建学校接口
def create_school_interface(school_name, school_addr, admin_name):
	# 查看当前学校是否已存在
	school_obj = models.School.select(school_name)

	# 若学校存在，则返回False，告知用户学校已存在
	if school_obj:
		return False, '学校已存在'

	# 若学校不存在，则创建学校，有管理员来创建学校
	# 创建管理员对象admin_obj
	admin_obj = models.Admin.select(admin_name)
	# 由管理员来创建学校方法,并传入学校的名称和地址
	admin_obj.create_school(school_name, school_addr)

	# 返回创建学校成功给视图层
	return True, f'{school_name} 学校创建成功！'


# 管理员创建课程接口
def create_course_interface(school_name, course_name, admin_name):
	# 1、查看要创建的课程是否已存在
	# 获取学校对象，然后进行判断，学校对象是有课程列表这个属性的
	school_obj = models.School.select(school_name)
	# 判断当前课程是否存在课程列表中
	if school_name in school_obj.course_list:
		return False, '当前课程已存在'
	else:
		# 若课程不存在，则创建课程，由管理员来创建
		# 获取管理员对象
		admin_obj = models.Admin.select(admin_name)
		admin_obj.create_course(school_obj, course_name)
		return True, f'{course_name}课程创建成功，绑定给{school_name}校区！'


# 管理员创建老师接口
def create_teacher_interface(teacher_name, admin_name, teacher_pwd='123'):
	# 判断老师是否已存在
	teacher_obj = models.Teacher.select(teacher_name)
	# 若存在，则返回不能创建
	if teacher_obj:
		return False, '老师已存在'
	# 若不存在，则由管理员进行老师创建
	# 先获取管理员对象
	admin_obj = models.Admin.select(admin_name)
	admin_obj.create_teacher(teacher_name, teacher_pwd)
	return True, f'{teacher_name} 老师创建成功！'












