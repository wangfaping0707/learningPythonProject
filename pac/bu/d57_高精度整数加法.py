while True:
	try:
		# n1 = '7844746'
		# n2 = '3267486'

		n1 = input().strip()
		n2 = input().strip()
		# 计算两个输入字符数字的长度
		n1_len = len(n1)
		n2_len = len(n2)

		# 判断两个字符长度，短的进行部位对齐
		if n1_len >= n2_len:
			n2 = n2.rjust(n1_len, '0')
		else:
			n1 = n1.rjust(n2_len, '0')

		# 将字符数字反转，然后转换位数字，并形成列表
		temp_n1 = list(map(int, n1[::-1]))
		temp_n2 = list(map(int, n2[::-1]))

		res = []
		# 进位数变量
		tag = 0
		for i in range(len(temp_n1)):
			if temp_n1[i] + temp_n2[i] + tag > 9:
				r = temp_n1[i] + temp_n2[i] + tag - 10
				res.append(r)
				tag = 1
			else:
				r = temp_n1[i] + temp_n2[i] + tag
				res.append(r)
				tag = 0
		# 判断最后一位数字相加，如果和大于1，则需要在添加一个1
		if tag:
			res.append('1')

		res = list(map(str, res))
		print(''.join(res)[::-1])

	except:
		break
