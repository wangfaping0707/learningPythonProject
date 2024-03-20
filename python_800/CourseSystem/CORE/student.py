"""
学生视图
"""

from LIB import common
from INTERFACE import common_interface
from INTERFACE import student_interface

student_info = {
	'user': ''
}


# 学生注册
def register():
	while True:
		username = input("请输入用户名：").strip()
		password = input("请输入密码：").strip()
		re_password = input("请确认密码：").strip()
		if password == re_password:
			# 调用接口层，学生注册接口
			flag, msg = student_interface.student_register_interface(username, password)
			if flag:
				print(msg)
				break
			else:
				print(msg)
		else:
			print('两次输入的密码不一致，请重新输入！')


# 学生登录
def login():
	while True:
		username = input('请输入要登陆的用户名：').strip()
		password = input('请输入密码：').strip()
		# 调用公共登录接口，进行登录操作
		flag, msg = common_interface.login_interface(username, password, user_type='student')
		# 对登录接口进行逻辑判定
		if flag:
			print(msg)
			# 记录当前登录的学生信息
			student_info['user'] = username
			break
		else:
			print(msg)


# 学生选择学校
@common.auth('student')
def choose_school():
	while True:
		# 获取所有学校，让学生进行选择
		flag, school_list = common_interface.get_all_school_interface()
		# 对获取的结果进行判断
		if not flag:
			print(school_list)
			break
		for index, school_name in enumerate(school_list):
			print(f'学校编号：{index}  学校名：{school_name}')
		# 让学生进行选择，并对选择的结果进行判定
		choice = input('请输入要选择的学校编号：').strip()
		if not choice.isdigit():
			print('输入有误，请重新输入！')
			continue
		# 对choice进行类型转换
		choice = int(choice)
		# 对输入的编号数字进行范围判定
		if choice not in range(len(school_list)):
			print('输入的编号有误，需要重新输入！')
			continue
		# 获取到选择的学校名称
		school_name = school_list[choice]
		# 开始调用学生的选择学校接口，并且要记录是那个学生选择的
		flag, msg = student_interface.add_school_interface(school_name, student_info.get('user'))
		if flag:
			print(msg)
			break
		else:
			print(msg)


# 学生注选择课程
@common.auth('student')
def choose_course():
	while True:
		# 1、先获取当前学生 所在学校的课程列表
		flag, course_list = student_interface.get_course_list_interface(student_info.get('user'))
		if not flag:
			print(course_list)
			break
		# 打印课程列表，让用户进行选择
		for index, course_name in enumerate(course_list):
			print(f'课程编号：{index}, 课程名称：{course_name}')
		# 让用户输入要选择的课程编号
		choice = input('请输入要选择的课程编号：').strip()
		if not choice.isdigit():
			print('课程编号输入有误，请重新输入！')
			continue
		choice = int(choice)
		if choice not in range(len(course_list)):
			print('课程编号不正确，请重新输入！')
			continue
		# 获取选择的课程名称
		course_name = course_list[choice]
		# 调用学生选择课程接口
		flag, msg = student_interface.add_course_interface(course_name, student_info.get('user'))
		if flag:
			print(msg)
			break
		else:
			print(msg)


# 学生查看课程分数
@common.auth('student')
def check_score():
	score_dict = student_interface.check_score_interface(student_info.get('user'))
	if not score_dict:
		print('没有选择课程！')
	else:
		print(score_dict)


func_dict = {
	'1': register,
	'2': login,
	'3': choose_school,
	'4': choose_course,
	'5': check_score
}


def student_view():
	while True:
		print('''
		1、注册
		2、登录功能
		3、选择校区
		4、选择课程
		5、查看分数
		''')
		choice = input('请输入功能编号：').strip()
		if choice == 'q':
			print('正在执行推出，请稍等。')
			break
		if choice not in func_dict:
			print('输入有误，请重新输入！')
			continue
		func_dict.get(choice)()
