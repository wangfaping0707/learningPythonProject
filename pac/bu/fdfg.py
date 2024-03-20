while True:
	try:
		# 总人数
		n = int(input().strip())
		# 确诊病例人员编号
		m1, m2 = input().strip().split(',')
		# 生成接触二维数组
		res = []
		for i in range(n):
			res.append(list(input().strip().split(',')))

		# 需要做核酸的人
		total = []
		# 0 表示没有接触，1 表示有接触,
		for i in range(len(res)):
			if str(i) == m1 or str(i) == m2:
				continue
			else:
				if res[i][i] == '1':
					total.append(i)

		# 需要做核算的人数
		total_num = len(total)
		print(total_num)

	except:
		break
