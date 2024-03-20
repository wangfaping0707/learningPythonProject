while True:
	try:
		s1 = input().strip()
		s2 = input().strip()
		n1 = len(s1)
		n2 = len(s2)
		# 初始化数组dp
		dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
		print(dp)
		# 初始化边界
		for i in range(1, n1 + 1):
			dp[i][0] = i
		print(dp)
		for j in range(1, n2 + 1):
			dp[0][j] = j
		print(dp)
		# 遍历两个字符串
		for i in range(1, n1 + 1):
			for j in range(1, n2 + 1):
				if s1[i - 1] == s2[j - 1]:
					dp[i][j] = dp[i - 1][j - 1]
				else:
					dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
		print(dp[n1][n2])
	except:
		break
