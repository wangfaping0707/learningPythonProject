"""
老师视图
"""
from LIB import common
from INTERFACE import common_interface
from INTERFACE import teacher_interface

teacher_info = {
	'user': ''
}


# 老师登录
def login():
	while True:
		username = input('请输入要登陆的用户名：').strip()
		password = input('请输入密码：').strip()
		# 调用公共登录接口，进行登录操作
		flag, msg = common_interface.login_interface(username, password, user_type='teacher')
		# 对登录接口进行逻辑判定
		if flag:
			print(msg)
			# 记录当前登录的学生信息
			teacher_info['user'] = username
			break
		else:
			print(msg)


# 查看教授课程
@common.auth('teacher')
def check_course():
	flag, course_list = teacher_interface.check_course_interface(teacher_info.get('user'))
	# 对返回的课程列表值进行判断
	if flag:
		print(course_list)
	else:
		print(course_list)


# 选择教授课程
@common.auth('teacher')
def pick_course():
	while True:
		# 先获取所有学校，然后进行学校选择
		flag, school_list = common_interface.get_all_school_interface()
		if not flag:
			print(school_list)
			break
		for index, school_name in enumerate(school_list):
			print(f'学校编号：{index}  学校名：{school_name}')
		choice = input('请输入要选择的学校编号：').strip()
		if not choice.isdigit():
			print('学校编号只能为数字')
			continue
		# 将输入的编号转换为数字
		choice = int(choice)
		if choice not in range(len(school_list)):
			print('输入的学校编号不在可选择范围内，请重新输入')
			continue
		# 获取选择的学校名称
		school_name = school_list[choice]

		# 从选择的学校中  获取所有课程
		flag1, course_list = common_interface.get_course_in_school_interface(school_name)
		if not flag1:
			print(course_list)
			break
		# 让老师在返回的课程列表当中进行课程选择
		for index1, course_name in enumerate(course_list):
			print(f'编号：{index1}  课程名：{course_name}')
		choice1 = input('请输入要选择的课程编号：').strip()
		if not choice1.isdigit():
			print('课程编号只能为数字')
			continue
		# 将输入的编号转换为数字
		choice1 = int(choice1)
		if choice1 not in range(len(course_list)):
			print('输入的课程编号不在可选择范围内，请重新输入')
			continue
		# 获取选择的课程名称
		course_name = course_list[choice1]

		# 调用选择教授课程接口，将课程添加到老师课程列表中
		flag2, msg = teacher_interface.add_course_interface(course_name, teacher_info.get('user'))
		if flag2:
			print(msg)
			break
		else:
			print(msg)


# 查看课程下学生
@common.auth('teacher')
def check_stu_from_course():
	while True:
		# 获取当前老师名下所有的课程:调用老师查看课程接口
		flag, course_list = teacher_interface.check_course_interface(teacher_info.get('user'))
		if not flag:
			print(course_list)
			break

		# 让老师在返回的课程列表当中进行课程选择
		for index, course_name in enumerate(course_list):
			print(f'编号：{index}  课程名：{course_name}')
		choice = input('请输入要选择的课程编号：').strip()
		if not choice.isdigit():
			print('课程编号只能为数字')
			continue
		# 将输入的编号转换为数字
		choice = int(choice)
		if choice not in range(len(course_list)):
			print('输入的课程编号不在可选择范围内，请重新输入')
			continue
		# 获取选择的课程名称
		course_name = course_list[choice]

		# 利用当前课程名，获取所有学生
		flag, student_list = teacher_interface.get_student_interface(course_name, teacher_info.get('user'))
		if flag:
			print(student_list)
			break
		else:
			print(student_list)


# 修改学生分数
@common.auth('teacher')
def change_score():
	"""
	1.先获取老师名下所有的课程,并进行课程选择;
	2.获取课程下所有的学生,并选择修改的学生;
	3.调用修改学生分数接口;
	"""
	while True:
		# 获取当前老师名下所有的课程:调用老师查看课程接口
		flag, course_list = teacher_interface.check_course_interface(teacher_info.get('user'))
		if not flag:
			print(course_list)
			break

		# 让老师在返回的课程列表当中进行课程选择
		for index, course_name in enumerate(course_list):
			print(f'编号：{index}  课程名：{course_name}')
		choice = input('请输入要选择的课程编号：').strip()
		if not choice.isdigit():
			print('课程编号只能为数字')
			continue
		# 将输入的编号转换为数字
		choice = int(choice)
		if choice not in range(len(course_list)):
			print('输入的课程编号不在可选择范围内，请重新输入')
			continue
		# 获取选择的课程名称
		course_name = course_list[choice]

		# 利用当前课程名，获取所有学生
		flag, student_list = teacher_interface.get_student_interface(course_name, teacher_info.get('user'))
		if not flag:
			print(student_list)
			break
		# 打印所有学生,让老师进行选择
		for index3, student_name in enumerate(student_list):
			print(f'学生编号:{index3}  学生姓名:{student_name}')
		choice3 = input('请输入要选择的学生编号:').strip()
		if not choice3.isdigit():
			print('学生编号是数字,请重新输入!')
			continue
		choice3 = int(choice3)
		if choice3 not in range(len(student_list)):
			print('输入的学生编号不在可选择的范围内,需要重新输入!')
			continue
		# 获取选择的学生的姓名
		student_name = student_list[choice3]

		# 让老师输入要修改的分数
		score = input('请输入要修改的分数:').strip()
		if not score.isdigit():
			print('分数需要为数字')
			continue
		# 将输入的分数转化为数字
		score = int(score)

		# 调用修改分数接口,进行分数修改
		flag4, msg = teacher_interface.change_score_interface(course_name, student_name, score, teacher_info.get('user'))
		if flag4:
			print(msg)
			break










func_dict = {
	'1': login,
	'2': check_course,
	'3': pick_course,
	'4': check_stu_from_course,
	'5': change_score
}


def teacher_view():
	while True:
		print('''
		1、登录
		2、查看教授课程
		3、选择教授课程
		4、查看课程下学生
		5、修改学生分数
		''')
		choice = input('请输入功能编号：').strip()
		if choice == 'q':
			print('正在执行推出，请稍等。')
			break
		if choice not in func_dict:
			print('输入有误，请重新输入！')
			continue
		func_dict.get(choice)()
