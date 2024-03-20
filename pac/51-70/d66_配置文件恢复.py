while True:
	try:
		# 输入的指令
		cmd = input().strip().split()
		# 命令转换字典
		dic_cmd = {'reset': 'reset what', 'reset board': 'board fault', 'board add': 'where to add',
		           'board delete': 'no board at all', 'reboot backplane': 'impossible',
		           'backplane abort': 'install first'}
		if len(cmd) < 0 or len(cmd) > 2:
			print('unknown command')
		elif len(cmd) == 1:
			if cmd[0] == 'reset'[0:len(cmd[0])]:
				print(dic_cmd['reset'])
			else:
				print('unknown command')
		else:
			# 存储匹配到的命令
			res = []
			for key in dic_cmd.keys():
				if key == 'reset':
					continue
				else:
					k_list = key.split()
					if cmd[0] == k_list[0][0:len(cmd[0])] and cmd[1] == k_list[1][0:len(cmd[1])]:
						res.append(key)
			# 例如输入：r b，找到匹配命令reset board和 reboot backplane，执行结果为：unknown command
			if len(res) != 1:
				print('unknown command')
			else:
				print(dic_cmd[res[0]])

	except:
		break