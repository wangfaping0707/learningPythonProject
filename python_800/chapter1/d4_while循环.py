# count = 0
# while count < 5:
# 	print(count)
# 	count += 1


# 登录小程序运行
user_name = 'egon'
pass_word = '123456'

tag = True
while tag:
	name = input('请输入用户名：')
	pwod = input('请输入密码：')
	if name == user_name and pwod == pass_word:
		print('恭喜您，登录成功')
		tag = False
	else:
		print('账号或密码错误，请重新登录')
