def login():
	print('登录功能')


def transfer():
	print('转账功能')


def check_balance():
	print("查询余额")


def withdraw():
	print('提现功能')


def register():
	print("注册功能")


dict_func = {'1': login, '2': transfer, '3': check_balance, '4': withdraw, '5': register}

while True:
	print("""请按照提示使用以下指令：
	0 退出
	1 登录
	2 转账
	3 查询余额
	4 提现
	5 注册
	""")
	choice = input('请输入您要执行的操作指令：').strip()
	if not choice.isdigit():
		print('请输入数字指令，二货')
		continue

	if choice == '0':
		break

	if choice in dict_func:
		dict_func[choice]()
	else:
		print('您输入的指令不存在')
