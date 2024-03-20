def auth(func):
	def wrapper(*args, **kwargs):
		name = input('请输入账号：')
		pwd = input('请输入密码：')
		if name == 'egon' and pwd == '123':
			res = func(*args, **kwargs)
			return res
		else:
			print('账号密码错误！！！')
	return wrapper

@auth
def index():
	print('from index hahaha')


index()