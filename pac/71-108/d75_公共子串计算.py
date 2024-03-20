while True:
	try:
		# s1 = 'asdfas'
		# s2 = 'werasdfaswer'
		s1 = input().strip()
		s2 = input().strip()

		len_s1 = len(s1)
		len_s2 = len(s2)
		if len_s1 > len_s2:
			s1, s2 = s2, s1

		# 存储最长 子字符串
		res = ''
		# 最长子字符串长度
		max_len = 0

		for L in range(len(s1) + 1):
			for j in range(0, len(s1) - L + 1):
				sub = s1[j:j + L]
				if sub in s2 and len(sub) > len(res):
					res = sub
					max_len = len(sub)

		print(max_len)
	except:
		break
