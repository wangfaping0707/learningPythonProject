while True:
	reply = input('请输入内容：')
	if reply == 'stop':
		break
	elif not reply.isdigit():
		print('字符串是不能参与运算的，请知悉！！!')
	else:
		print(int(reply)**2)
print('脚本练习结束')











