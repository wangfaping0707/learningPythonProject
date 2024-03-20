while True:
	try:
		# s = 'abcd12345ed125ss123058789'
		s = input().strip()
		for i in s:
			if not i.isdigit():
				s = s.replace(i, ' ')
		num_list = s.split()
		max_len = 0
		res = ''
		for j in num_list:
			if len(j) > max_len:
				max_len = len(j)

		for s in num_list:
			if len(s) == max_len:
				res += s

		print(f'{res},{max_len}')
	except:
		break

