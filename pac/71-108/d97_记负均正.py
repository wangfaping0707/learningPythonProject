while True:
	try:
		# 整数个数n
		n = int(input().strip())

		num_list = list(map(int, input().strip().split()))

		# 大于0的数
		num1 = []
		# 记录小于0的数据对应的个数
		count = 0
		for i in num_list:
			if i > 0:
				num1.append(i)
			elif i < 0:
				count += 1
			else:
				continue

		# 大于0数据的平均数
		if sum(num1) > 0:
			average_val = round(sum(num1) / len(num1), 1)
		else:
			average_val = 0.0

		print(count, '{:.1f}'.format(average_val))

	except:
		break
