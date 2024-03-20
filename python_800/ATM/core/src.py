"""
存放用户视图层
"""
from interface import user_interface
from interface import bank_interface
from lib import common

# 全局变量：login_user = None
login_user = None


# 1、注册功能
def register():
	while True:
		# 让用户输入用户名和密码进行校验
		username = input('请输入用户名：').strip()
		password = input('请输入密码：').strip()
		re_password = input('请确认密码：').strip()

		# 小的逻辑处理，判断两次输入的密码是否一致
		if password == re_password:
			# 调用接口层的注册接口，将用户输入的数据 交给接口进行处理
			flag, msg = user_interface.register_interface(username, password)
			# 根据 接口层 返回的flag来判断用户是否注册成功,用于控制break
			if flag:
				print(msg)
				break
			else:
				print(msg)


# 2、登录功能
def login():
	while True:
		# 让用户输入用户名和密码
		username = input('请输入用户名：').strip()
		password = input('请输入密码：').strip()
		# 调用接口层，将用户输入的用户名和密码传给登录接口
		flag, msg = user_interface.login_interface(username, password)
		if flag:
			print(msg)
			global login_user
			login_user = username
			break
		else:
			print(msg)


# 3、查看余额
@common.login_auth
def check_balance():
	# 直接调用逻辑层的查询余额接口，获取该用户名下的余额
	balance = user_interface.check_bal_interface(login_user)
	print(f'用户{login_user}的余额为：{balance}')


# 4、提现功能
@common.login_auth
def withdraw():
	while True:
		# 让用户输入要提现的金额
		input_money = input('请输入要提现的金额：').strip()
		# 对用户输入的金额进行校验，判断是否为数字
		if not input_money.isdigit():
			print('提现的金额需要为数字，请重新输入！！！')
			continue
		else:
			# 用户提现的金额，将提现的逻辑交给接口层来处理
			flag, msg = bank_interface.withdraw_interface(login_user, input_money)
			if flag:
				print(msg)
				break
			else:
				print(msg)


# 5、还款功能
@common.login_auth
def repay():
	while True:
		# 让用户输入要还款的金额，并对用户的输入要进行校验
		input_money = input('请输入要还款的金额：').strip()
		if not input_money.isdigit():
			print('还款金额请输入数字，谢谢！！！')
			continue
		input_money = int(input_money)
		if input_money > 0:
			# 调用还款接口
			flag, msg = bank_interface.repay_interface(login_user, input_money)
			if flag:
				print(msg)
				break
		else:
			print('输入的还款金额不能小于0')


# 6、转账功能
@common.login_auth
def transfer():
	while True:
		# 1、接收用户输入的转账金额
		# 2、接收用户输入的转账 目标用户
		to_user = input('请输入转账目标用户：').strip()
		money = input('请输入要转账的金额：').strip()
		# 判断用户输入的金额是否是大于0的数字
		if not money.isdigit():
			print('转账金额需要数字，请重新输入！')
			continue
		money = int(money)
		if money > 0:
			flag, msg = bank_interface.transfer_interface(
				# 当前用户，目标用户，转账金额
				login_user, to_user, money
			)
			if flag:
				print(msg)
				break
			else:
				print(msg)
		else:
			print('转账金额需要大于0，请重新输入！')


# 7、查看流水
@common.login_auth
def check_flow():
	# 直接调用查看流水接口
	flow_list = bank_interface.check_flow_interface(login_user)
	if flow_list:
		for flow in flow_list:
			print(flow)
	else:
		print('当前用户没有流水')


# 8、购物功能
@common.login_auth
def shopping():
	# 新建一个商品列表
	shop_list = [
		['水蜜桃', 16.8],
		['西瓜', 10.50],
		['荔枝', 26.8],
		['菠萝', 9.9],
		['丑橘', 19.8],
		['哈密瓜', 11.8]
	]

	# 初始化用户的购物车, 存储的数据格式可以为 {'商品名称'：['单价','数量']}
	shop_car = {}

	while True:
		# 1、打印商品信息，让用户选择
		# 2、枚举：enumerate(可迭代对象)----->(可迭代索引，索引对应的值)
		# 3、枚举：enumerate(可迭代对象)----->(0, ['水蜜桃', 16.8])
		for index, shop in enumerate(shop_list):
			shop_name, shop_price = shop
			print(
				f'商品的编号为：{index}',
				f'商品的名称为：{shop_name}',
				f'商品的价格为：{shop_price}'
			)
		# 让用户根据商品编号进行选择
		choice = input('请输入要购买的商品编号 (是否结账输入y or n)：').strip()
		# 如果输入的是y，则进入支付结算功能
		if choice == 'y':
			# 调用支付接口进行结算
			if not shop_car:
				print('购物车是空的，不能支付，请重新输入！')
				continue
			# 调用支付接口进行支付

		# 如果输入的是n，添加购物车
		elif choice == 'n':
			# 判断当前用户是否添加过购物车
			if not shop_car:
				print('购物车是空的，不能添加，请重新输入！')
				continue



		if not choice.isdigit():
			print('请输入数字类型的编号，二货！！！')
			continue
		# 将字符型数字编号转化为数字型编号
		choice = int(choice)
		# 判断输入的choice是否存在
		if choice not in range(len(shop_list)):
			print('请输入在提示的商品编号，蠢货！！！')
			continue
		# 获取商品名称和单价
		shop_name, shop_price = shop_list[choice]
		# 加入购物车:判断选择的商品在购物车中是否已存在，已存在，则购买数量加一，如果不存在，默认商品数量为1
		if shop_name in shop_car:
			shop_car[shop_name][1] += 1
		else:
			shop_car[shop_name] = [shop_price, 1]





# 9、查看购物车
@common.login_auth
def check_shop_car():
	pass


# 10、管理员功能
@common.login_auth
def admin():
	from core import admin
	admin.admin_run()


# 创建函数功能字典
func_dic = {
	'1': register,
	'2': login,
	'3': check_balance,
	'4': withdraw,
	'5': repay,
	'6': transfer,
	'7': check_flow,
	'8': shopping,
	'9': check_shop_car,
	'10': admin
}


# 视图层主程序
def run():
	while True:
		print(
			'''
		=====ATM + 购物车===============	
			1、注册功能
			2、登录功能
			3、查看余额
			4、提现功能
			5、还款功能
			6、转账功能
			7、查看流水
			8、购物功能
			9、查看购物车
			10、管理员功能
		=====Send======================
			'''
		)
		choice = input("请输入功能编号：").strip()
		if choice not in func_dic:
			print('请输入正确的功能编号：')
			continue

		# 执行选择的功能函数
		func_dic.get(choice)()
