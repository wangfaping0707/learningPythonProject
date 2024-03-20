while True:
	try:
		s1 = input().strip()
		s2 = input().strip()

		if len(s1) > len(s2):
			s1, s2 = s2, s1
		# 存储最长的公共子 字符串
		max_str = ''

		# 从短的字符串s1中,开始截取子字符串:截取的字符串长度L 逐渐从1 增长
		for L in range(1, len(s1) + 1):
			for j in range(len(s1) - L + 1):
				sub = s1[j:j + L]
				if sub in s2 and len(sub) > len(max_str):
					max_str = sub

		print(max_str)
	except:
		break
