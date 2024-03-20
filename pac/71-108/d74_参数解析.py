while True:
	try:
		# s = 'xcopy /s "C:\\program files" "d:\"'
		s = input().strip()

		flag = False
		new_s = ''
		for i in s:
			if i == '"':
				flag = not flag
			elif flag:
				if i == ' ':
					i = '0'
					new_s += i
				else:
					new_s += i
			else:
				new_s += i

		new_lst = new_s.split()
		print(len(new_lst))
		for i in new_lst:
			print(i.replace('0', ' '))
	except:
		break
