user_name = 'egon'
pass_word = '123'

for i in range(3):
	name = input("请输入用户名：")
	pwd = input("请输入登录密码：")
	if name == user_name and pwd == pass_word:
		print("恭喜您登陆成功")
		break

else:
	print('您输错密码的次数过多。。。。。')