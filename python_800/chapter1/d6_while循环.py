# 登录小程序运行
user_name = 'egon'
pass_word = '123456'
tag = True

while tag:
	name = input('请输入用户名：')
	pwod = input('请输入密码：')
	if name == user_name and pwod == pass_word:
		print('恭喜您，登录成功')
		while tag:
			cmd = input('请输入你要执行的操作：')
			if cmd == 'q':
				print('正在执行退出操作')
				tag = False
			else:
				print('程序正在执行{x}操作，请耐心等待，谢谢！'.format(x=cmd))
	else:
		print('账号或密码错误，请重新登录')
