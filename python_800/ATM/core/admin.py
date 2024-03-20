from core import src
from interface import admin_interface


# 添加用户
def add_user():
	src.register()


# 修改用户额度
def check_balance():
	while True:
		# 1、输入要修改的用户
		change_user = input('请输入需要修改额度的用户：').strip()
		# 2、用户需要修改的额度大小
		money = input('请输入需要修改的用户额度：').strip()
		if not money.isdigit():
			print('输入的额度需要为数字，请重新输入！')
			continue
		# 3、调用修改额度的接口
		flag, msg = admin_interface.change_balance_interface(
			change_user, money
		)
		if flag:
			print(msg)
			break
		else:
			print(msg)


# 冻结账户
def lock_user():
	while True:
		# 1、输入要冻结的用户
		change_user = input('请输入需要冻结的用户：').strip()
		flag, msg = admin_interface.lock_user_interface(change_user)
		if flag:
			print(msg)
			break
		else:
			print(msg)


# 管理员功能函数字典
admin_func = {
	'1': add_user,
	'2': check_balance,
	'3': lock_user
}


def admin_run():
	while True:
		print('''
		1、添加账户
		2、修改用户额度
		3、冻结账户
		''')
		choice = input('请输入要执行的功能编号:').strip()
		if choice not in admin_func:
			print('请输入正确的功能编号!')
			continue
		admin_func.get(choice)()
