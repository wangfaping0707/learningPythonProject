from collections.abc import Iterable

# 接受用户输入的账号和密码,同时除去前后空格
input_name = input("请输入账号：").strip()
input_pass = input("请输入密码：").strip()

# 从电脑硬盘中读取已存储的账号和密码
with open('file_package/user.txt', mode='rt', encoding='utf-8') as f:
	# print('判断f是否是一个可迭代对象：', isinstance(f, Iterable))
	for line in f:
		# 查看line内容是什么,由打印可知，读出来的是个字符串，可以拆分成列表
		# print(type(line))
		# print(line,end='')
		l = line.strip().split(':')
		# print(l)
		# 列表的解压赋值
		name, password = l
		if input_name == name and input_pass == password:
			print('Login Successful')
			break
	else:
		print('用户名或密码错误')
