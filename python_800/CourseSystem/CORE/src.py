from CORE import admin
from CORE import student
from CORE import teacher

func_dic = {
	'1': admin.admin_view,
	'2': student.student_view,
	'3': teacher.teacher_view
}


def run():
	while True:
		print('''
		======================欢迎来到选课系统======================
						1、管理员功能
						2、学生功能
						3、老师功能		
		=================END======================================
		''')
		choice = input('请输入要执行的功能编号：').strip()
		if choice not in func_dic:
			print('输入的功能编号有误，不在可选择范围内，请重新选择！')
			continue
		func_dic.get(choice)()
