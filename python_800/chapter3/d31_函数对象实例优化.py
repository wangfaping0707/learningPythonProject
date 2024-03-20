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


dict_func = {
	'0': ['退出', None],
	'1': ['登录', login],
	'2': ['转账', transfer],
	'3': ['查询余额', check_balance],
	'4': ['提现', withdraw],
	'5': ['注册', register]}

while True:
	for k in dict_func:
		print(k, dict_func[k][0])
	choice = input('请输入您要执行的操作指令：').strip()
	if not choice.isdigit():
		print('请输入数字指令，二货')
		continue

	if choice == '0':
		break

	if choice in dict_func:
		dict_func[choice][1]()
	else:
		print('您输入的指令不存在')
