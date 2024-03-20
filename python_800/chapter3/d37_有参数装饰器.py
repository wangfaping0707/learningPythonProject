def auth(db_type):
	# 受限与语法糖，所以deco函数不能改变传入的参数，参数格式被限制死了，所以只能通过闭包函数来传参，外面在包装一层函数
	def deco(func):
		def wrapper(*args, **kwargs):
			name = input("请入登录账号：").strip()
			pwd = input('请输入密码：').strip()
			if db_type == 'file':
				print('数据来源是file')
				if name == 'egon' and pwd == '123':
					print('login successful...')
					res = func(*args, **kwargs)
					return res
				else:
					print('账号或密码错误')
			elif db_type == 'mysql':
				print('数据来源是mysql')
				if name == 'egon' and pwd == '123':
					print('login successful...')
					res = func(*args, **kwargs)
					return res
				else:
					print('账号密码错误')
			elif db_type == 'lapd':
				print('数据来源是lapd')
				if name == 'egon' and pwd == '123':
					print('login successful...')
					res = func(*args, **kwargs)
					return res
				else:
					print('账号或密码错误')
			else:
				print('不支持该{}数据类型'.format(db_type))

		return wrapper

	return deco


"""
@auth(db_type='mysql') 这个要拆开分析 @ + auth(db_type='mysql')  右边的是带括号有参数，所以需要进行运行，运行回来的结果在和@符号进行联动
auth(db_type='mysql') 运行的结果是返回函数 deco，即@auth(db_type='mysql') = @deco
@deco语法糖就是无参数装饰器，即为执行deco(index)，返回结果为函数 wrapper所以可以写成 index = deco(index)
所以index('1','23')就是执行wrpper函数 wrapper('1','23')
"""


@auth(db_type='mysql')
def index(x, y):
	print("index=>>>>", x, y)


# 调用函数
index('888888', '999999')
